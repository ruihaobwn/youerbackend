from rest_framework.viewsets import ReadOnlyModelViewSet
from card.models import CardType
from card.serializers import CardTypeSerializer
from .. import filters


class CardTypeViewSet(ReadOnlyModelViewSet):
    filter_class = filters.CardTypeFilter
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerializer
