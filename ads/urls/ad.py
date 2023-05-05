from django.urls import path
from rest_framework import routers

from ads import views

router = routers.SimpleRouter()
router.register('ad', views.AdsViewSet)

urlpatterns = [
    path('<int:pk>/upload_image/', views.ApUploadImageView.as_view())
]

urlpatterns += router.urls
