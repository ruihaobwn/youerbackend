from django_filters import rest_framework as filters

from card import models


class CardTypeFilter(filters.FilterSet):
    product = filters.NumberFilter(field_name='product')

    class Meta:
        model = models.CardType
        fields = ['title']
