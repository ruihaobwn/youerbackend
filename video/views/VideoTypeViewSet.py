from rest_framework.viewsets import ReadOnlyModelViewSet
from video import models, serializers


class VideoTypeViewSet(ReadOnlyModelViewSet):
    queryset = models.VideoType.objects.all()
    serializer_class = serializers.VideoTypeSerializer
