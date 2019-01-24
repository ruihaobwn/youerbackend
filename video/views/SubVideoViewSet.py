from rest_framework.viewsets import ReadOnlyModelViewSet
from video import models, serializers
from .. import filters


class SubVideoViewSet(ReadOnlyModelViewSet):
    filter_class = filters.SubVideoFilter
    queryset = models.SubVideo.objects.all()
    serializer_class = serializers.SubVideoSerializer
