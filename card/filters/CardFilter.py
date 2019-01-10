from django_filters import rest_framework as filters
from card import models


class CardFilter(filters.FilterSet):
    card_type = filters.NumberFilter(field_name='card_type')

    class Meta:
        model = models.Card
        fields = ['name']
