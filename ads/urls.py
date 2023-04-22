from django.urls import path

from ads import views

urlpatterns = [
    path('', views.AdsListView.as_view()),
    path('<int:pk>/', views.AdDetailView.as_view()),
    path('create/', views.AdCreateView.as_view()),
    path('update/<int:pk>/', views.AdUpdateView.as_view()),
    path('delete/<int:pk>/', views.AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', views.ApUploadImageView.as_view()),
]