from card.models import Card
from common.serializers import BaseSerializer


class CardSerializer(BaseSerializer):
    class Meta:
        model = Card
        fields = (
            'id', 'name', 'picture', 'en_word_voice', 'am_word_voice', 'en_sentence_voice', 'am_sentence_voice',
            'video',
            'page_num')


class CardNameSerializer(BaseSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name',)
