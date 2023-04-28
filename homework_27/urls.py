from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from users import views

router = routers.SimpleRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ad/', include('ads.urls')),
    path('cat/', include('categories.urls')),
    path('user/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
