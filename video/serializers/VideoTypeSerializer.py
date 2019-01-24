from common.serializers import BaseSerializer
from video.models import VideoType


class VideoTypeSerializer(BaseSerializer):
    class Meta:
        model = VideoType
        fields = ('id', 'title', 'image_file')
