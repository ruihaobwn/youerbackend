from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from card.models import Card
from card.serializers import CardSerializer, CardNameSerializer
from .. import filters
import time
import hashlib
import requests
import json
import base64
from utils import CRS


class CardViewSet(ReadOnlyModelViewSet):
    filter_class = filters.CardFilter
    queryset = Card.objects.all().order_by('page_num')
    serializer_class = CardSerializer

    def get_serializer_class(self):
        params = self.request.query_params
        title = params.get('title')
        if title:
            return CardNameSerializer
        else:
            return CardSerializer

    @action(detail=False, methods=['post'])
    def recognize(self, request, *args, **kwargs):
        image = request.FILES.get("image", None)
        image_body = image.read()
        params = {
            "notracking": "true",
            "timestamp":int(time.time() * 1000),
            "appKey": CRS.CLOUDKEY,
            "image": base64.b64encode(image_body).decode()
        }
        params = {k: params[k] for k in sorted(params.keys())}
        tmp = []
        for key, value in params.items():
            tmp.append('{}{}'.format(key, value))

        string = ''.join(tmp)
        m = hashlib.sha256()
        m.update(string.encode('utf-8'))
        m.update(CRS.CLOUDSECRET.encode('utf-8'))
        params['signature'] = m.hexdigest()
        try:
            url = CRS.CLOUDCLIENTURL + '/search'
            res = requests.post(url, headers={'Content-Type': 'application/json', 'charset': 'utf-8'}, data=json.dumps(params))
            res.raise_for_status()
            result = res.json()['result']
            meta = result.get('target').get('meta')
            card_id = base64.b64decode(meta)
            card =  Card.objects.get(id=card_id)
            card_type_id = card.card_type.id
            return Response({"statusCode": 0, "id": card_id, "card_type_id": card_type_id, 'page_num': card.page_num})
        except requests.exceptions.HTTPError as e:
            return Response(res.json())
