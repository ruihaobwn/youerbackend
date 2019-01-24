from common.serializers import BaseSerializer
from video.models import Video


class VideoSerializer(BaseSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'image_file', 'video_url', 'has_subvideo')
