from common.serializers import BaseSerializer
from video.models import SubVideo


class SubVideoSerializer(BaseSerializer):
    class Meta:
        model = SubVideo
        fields = ('id', 'title', 'description', 'image_url',  'video_url')
