from rest_framework import routers
from video.views.VideoTypeViewSet import VideoTypeViewSet
from video.views.SubVideoViewSet import SubVideoViewSet
from video.views.VideoViewSet import VideoViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'video_type', VideoTypeViewSet)
router.register(r'subvideo', SubVideoViewSet)
router.register(r'video', VideoViewSet)
urlpatterns = router.urls
