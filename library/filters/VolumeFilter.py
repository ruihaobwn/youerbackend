from django_filters import rest_framework as filters
from library import models


class VolumeFilter(filters.FilterSet):
    class Meta:
        model = models.Volume
        fields = ['book_type']
