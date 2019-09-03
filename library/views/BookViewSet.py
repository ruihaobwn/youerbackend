from rest_framework.viewsets import ReadOnlyModelViewSet
from library import models, serializers
from .. import filters


class BookViewSet(ReadOnlyModelViewSet):
    filterset_class = filters.BookFilter
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class VolumeViewSet(ReadOnlyModelViewSet):
    filterset_class = filters.VolumeFilter
    queryset = models.Volume.objects.all()
    serializer_class = serializers.VolumeSerializer
