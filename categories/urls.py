from rest_framework import routers
from categories.views import CategoryViewSet

router = routers.SimpleRouter()
router.register('cat', CategoryViewSet)
urlpatterns = router.urls

# from django.urls import path
#
# from categories import views
#
# urlpatterns = [
#     path('', views.CategoriesListView.as_view()),
#     path('<int:pk>/', views.CategoryDetailView.as_view()),
#     path('create/', views.CategoryCreateView.as_view()),
#     path('update/<int:pk>/', views.CategoryUpdateView.as_view()),
#     path('delete/<int:pk>/', views.CategoryDeleteView.as_view())
#
# ]