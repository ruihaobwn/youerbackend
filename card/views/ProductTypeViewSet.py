from rest_framework.viewsets import ReadOnlyModelViewSet
from card.models import ProductType
from card.serializers import ProductTypeSerializer
from .. import filters


class ProductTypeViewSet(ReadOnlyModelViewSet):
    filter_class = filters.ProductTypeFilter
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
