from common.models import Poster
from common.serializers.BaseSerializer import BaseSerializer


class PosterSerializer(BaseSerializer):
    class Meta:
        model = Poster
        fields = ('id', 'name', 'type', 'image', 'link_url')
        read_only_fields = ('created_time', 'updated_time',)
