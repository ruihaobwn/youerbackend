from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from card.models import Card
from card.serializers import CardSerializer, CardNameSerializer
from .. import filters


class CardViewSet(ReadOnlyModelViewSet):
    filter_class = filters.CardFilter
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_serializer_class(self):
        params = self.request.query_params
        title = params.get('title')
        if title:
            return CardNameSerializer
        else:
            return CardSerializer
