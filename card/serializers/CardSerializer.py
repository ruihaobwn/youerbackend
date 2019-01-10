from card.models import Card
from common.serializers import BaseSerializer
from .CardAudioSerializer import CardAudioSerializer


class CardSerializer(BaseSerializer):
    card_audio = CardAudioSerializer(source="cardaudio_set", many=True, required=False, read_only=True)

    class Meta:
        model = Card
        fields = ('id', 'name', 'picture', 'card_audio', 'video')


class CardNameSerializer(BaseSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', )
