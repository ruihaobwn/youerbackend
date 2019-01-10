from django_filters import rest_framework as filters

from card import models


class ProductTypeFilter(filters.FilterSet):

    class Meta:
        model = models.ProductType
        fields = ['sup_type', 'sub_type']
