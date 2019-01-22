from rest_framework.viewsets import ReadOnlyModelViewSet
from library import models, serializers
from .. import filters


class BookPageViewSet(ReadOnlyModelViewSet):
    filter_class = filters.BookPageFilter
    queryset = models.BookPage.objects.all()
    serializer_class = serializers.BookPageSerializer
