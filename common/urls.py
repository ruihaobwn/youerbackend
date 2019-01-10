from rest_framework import routers
from common.views.PosterViewSet import PosterViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'poster', PosterViewSet)

urlpatterns = router.urls
