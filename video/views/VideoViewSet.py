from rest_framework.viewsets import ReadOnlyModelViewSet
from video import models, serializers
from .. import filters


class VideoViewSet(ReadOnlyModelViewSet):
    filter_class = filters.VideoFilter
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
