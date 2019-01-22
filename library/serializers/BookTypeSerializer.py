from common.serializers import BaseSerializer
from library.models import BookType


class BookTypeSerializer(BaseSerializer):
    class Meta:
        model = BookType
        fields = ('id', 'title', 'image_file')
