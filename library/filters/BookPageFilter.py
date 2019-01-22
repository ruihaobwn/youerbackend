from django_filters import rest_framework as filters
from library import models


class BookPageFilter(filters.FilterSet):
    class Meta:
        model = models.BookPage
        fields = ['volume', 'book']


class BookFilter(filters.FilterSet):
    class Meta:
        model = models.Book
        fields = ['volume']
