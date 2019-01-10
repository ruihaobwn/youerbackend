from django_filters import rest_framework as filters

from common import models


class PosterFilter(filters.FilterSet):

    class Meta:
        model = models.Poster
        fields = ['type']
