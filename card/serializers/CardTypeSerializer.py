from card.models import CardType
from common.serializers.BaseSerializer import BaseSerializer


class CardTypeSerializer(BaseSerializer):
    class Meta:
        model = CardType
        fields = ('id', 'title', 'image_file')