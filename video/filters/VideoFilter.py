from django_filters import rest_framework as filters
from video import models


class VideoFilter(filters.FilterSet):
    class Meta:
        model = models.Video
        fields = ['video_type']
