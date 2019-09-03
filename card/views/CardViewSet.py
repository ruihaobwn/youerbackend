from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from card.models import Card
from card.serializers import CardSerializer
from card.serializers.CardSerializer import CardVideoSerializer
from .. import filters
from django.core.files.storage import FileSystemStorage
import time
import hashlib
import requests
import json
import base64
from utils import CRS, OCR
from utils.ApiOcr import client
from django.conf import settings
from utils import Turi
import logging

log = logging.getLogger(__name__)


class CardViewSet(ReadOnlyModelViewSet):
    filterset_class = filters.CardFilter
    queryset = Card.objects.all().order_by('page_num')
    serializer_class = CardSerializer

    def get_serializer_class(self):
        params = self.request.query_params
        video = params.get('video')
        if video:
            return CardVideoSerializer
        return CardSerializer

    @action(detail=False, methods=['post'])
    def recognize(self, request, *args, **kwargs):
        image = request.FILES.get("image", None)
        image_body = image.read()
        params = {
            "notracking": "true",
            "timestamp": int(time.time() * 1000),
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
            log.debug(url)
            res = requests.post(url, headers={'Content-Type': 'application/json', 'charset': 'utf-8'},
                                data=json.dumps(params))
            res.raise_for_status()
            result = res.json()['result']
            log.debug(result)
            card_id = result.get('target').get('meta')
            card = Card.objects.get(id=card_id)
            card_type = card.card_type
            card_type_id = card_type.id
            voice_num = card_type.voice_num
            return Response({"statusCode": 0, "id": card_id, "type_id": card_type_id, 'page_num': card.page_num,
                             'voice_num': voice_num})
        except requests.exceptions.HTTPError as e:
            log.error(e)
            return Response({"statusCode": -1})

    @action(detail=False, methods=['post'])
    def word_recognize(self, request, *arg, **kwargs):
        image = request.FILES["image"]
        image_path = '{}/recognize'.format(settings.MEDIA_ROOT)
        fs = FileSystemStorage(location=image_path)
        filename = fs.save(image.name, image)
        image_recognize_id = Turi.find_image('{}/{}'.format(image_path, filename))
        print(image_recognize_id)
        card = Card.objects.get(recognize_id=image_recognize_id)
        card_type = card.card_type
        card_type_id = card_type.id
        voice_num = card_type.voice_num
        return Response({"statusCode": 0, "id": card.id, "type_id": card_type_id, 'page_num': card.page_num,
                         'voice_num': voice_num})

    @action(detail=False, methods=['post'])
    def image_recognize(self, request, *arg, **kwargs):
        image = request.FILES.get("image", None)
        image_body = image.read()
        res = client.basicGeneral(image_body)
        recognize_str = res["words_result"][0]["words"]
        card_set = Card.objects.filter(recognize_word__iexact=recognize_str)
        card_num = card_set.count()
        if card_num == 0:
            return Response(status=404)
        if card_num == 1:
            card = card_set[0]
        else:
            index_list = list(range(card_num))
            for words in res['words_result']:
                if len(index_list) <= 1:
                    break
                filter_list = []
                for index in index_list:
                    recognize_list = json.loads(card_set[index].recognize_text)
                    if words["words"] not in recognize_list:
                        filter_list.append(index)
                index_list = [x for x in index_list if x not in filter_list]

            if len(index_list) == 0:
                return Response(status=404)
            if len(index_list) == 1:
                card = card_set[index_list[0]]
            else:
                return Response(404)
        card_type = card.card_type
        card_type_id = card_type.id
        voice_num = card_type.voice_num
        return Response({"statusCode": 0, "id": card.id, "type_id": card_type_id, 'page_num': card.page_num,
                         'voice_num': voice_num})
        return Response(res)
