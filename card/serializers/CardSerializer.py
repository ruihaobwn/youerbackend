from card.models import Card
from common.serializers import BaseSerializer


class CardSerializer(BaseSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'picture', 'word_voice', 'sentence_voice', 'video')


class CardNameSerializer(BaseSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', )
