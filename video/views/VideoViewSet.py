from rest_framework.viewsets import ReadOnlyModelViewSet
from video import models, serializers
from django.http import HttpResponse
from django.template import loader
from .. import filters
import logging
from django.conf import settings


log = logging.getLogger(__name__)


class VideoViewSet(ReadOnlyModelViewSet):
    filter_class = filters.VideoFilter
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer

    def retrieve(self, request, pk=None):
        video = self.get_object()
        template = loader.get_template('video.html')
        url = "{site_url}/media/{video_url}".format(site_url=settings.SITE_URL, video_url=video.video_url)
        log.debug(url)
        context = {
            'video_url': url,
        }
        return HttpResponse(template.render(context, request))
        
        
