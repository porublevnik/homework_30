from rest_framework import routers
from ads.views import SelectionViewSet

router = routers.SimpleRouter()
router.register('selection', SelectionViewSet)
urlpatterns = router.urls
