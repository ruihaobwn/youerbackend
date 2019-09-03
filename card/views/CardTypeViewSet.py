from rest_framework.viewsets import ReadOnlyModelViewSet
from card.models import CardType
from card.serializers import CardTypeSerializer
from rest_framework.response import Response

from .. import filters


class CardTypeViewSet(ReadOnlyModelViewSet):
    filterset_class = filters.CardTypeFilter
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerializer

    def list(self, request, *args, **kwargs):
        params = self.request.query_params
        list_tag = params.get('list_tag')
        if list_tag:
            tags = CardType.objects.filter(product=params.get('product')).order_by('tag_order').distinct().values_list('tag', flat=True)
            # remove None
            tags = filter(None, tags)
            tags = list(tags)
            return Response(data=tags)
        return super(CardTypeViewSet, self).list(request, *args, **kwargs)

