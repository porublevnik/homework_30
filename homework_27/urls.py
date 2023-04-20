"""
URL configuration for homework_27 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ads.views import IndexView, CategoriesListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView,\
    CategoryDeleteView,  AdsListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, ApUploadImageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),

    path('cat/', CategoriesListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('cat/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('cat/delete/<int:pk>/', CategoryDeleteView.as_view()),

    path('ad/', AdsListView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/update/<int:pk>/', AdUpdateView.as_view()),
    path('ad/delete/<int:pk>/', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', ApUploadImageView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
