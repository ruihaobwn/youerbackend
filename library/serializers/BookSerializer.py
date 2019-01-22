from common.serializers import BaseSerializer
from library.models import Book, Volume


class VolumeSerializer(BaseSerializer):
    class Meta:
        model = Volume
        fields = ('id', 'name', 'picture', 'book_type', 'has_subbook')


class BookSerializer(BaseSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'picture', 'description')
