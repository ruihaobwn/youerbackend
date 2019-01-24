from django_filters import rest_framework as filters
from video import models


class SubVideoFilter(filters.FilterSet):
    class Meta:
        model = models.SubVideo
        fields = ['video']
