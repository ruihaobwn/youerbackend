from rest_framework.viewsets import ReadOnlyModelViewSet
from library import models, serializers


class BookTypeViewSet(ReadOnlyModelViewSet):
    queryset = models.BookType.objects.all()
    serializer_class = serializers.BookTypeSerializer
