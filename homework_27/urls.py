from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ads.urls.ad')),
    path('cat/', include('categories.urls')),
    path('user/', include('users.urls.user')),
    path('', include('users.urls.location')),
    path('', include('ads.urls.selection')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

