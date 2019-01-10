from common.serializers import BaseSerializer
from card.models import CardAudio


class CardAudioSerializer(BaseSerializer):
    class Meta:
        model = CardAudio
        fields = ('id', 'type', 'url')
