from rest_framework.viewsets import ReadOnlyModelViewSet
from library import models, serializers
from .. import filters


class BookPageViewSet(ReadOnlyModelViewSet):
    filterset_class = filters.BookPageFilter
    queryset = models.BookPage.objects.all().order_by('page_num')
    serializer_class = serializers.BookPageSerializer
