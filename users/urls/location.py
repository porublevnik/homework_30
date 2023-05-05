from django.urls import path
from rest_framework import routers

from users import views

router = routers.SimpleRouter()
router.register('location', views.LocationViewSet)
urlpatterns = router.urls