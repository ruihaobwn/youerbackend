from rest_framework import routers
from library.views.BookPageViewSet import BookPageViewSet
from library.views.BookTypeViewSet import BookTypeViewSet
from library.views.BookViewSet import BookViewSet, VolumeViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'book_type', BookTypeViewSet)
router.register(r'volume', VolumeViewSet)
router.register(r'book', BookViewSet)
router.register(r'bookpage', BookPageViewSet)
urlpatterns = router.urls
