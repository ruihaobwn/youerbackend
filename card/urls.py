from rest_framework import routers
from card.views.ProductTypeViewSet import ProductTypeViewSet
from card.views.CardTypeViewSet import CardTypeViewSet
from card.views.CardViewSet import CardViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'product_type', ProductTypeViewSet)
router.register(r'card_type', CardTypeViewSet)
router.register(r'card', CardViewSet)
urlpatterns = router.urls
