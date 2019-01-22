from common.serializers import BaseSerializer
from library.models import BookPage


class BookPageSerializer(BaseSerializer):
    class Meta:
        model = BookPage
        fields = ('id', 'title', 'picture', 'audio_url')
