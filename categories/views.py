import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.serializers import CategorySerializer
from homework_27 import settings

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request):

        return JsonResponse({"status": "ok"}, status=200)


# @method_decorator(csrf_exempt, name='dispatch')
# class CategoriesListView(ListView):
#     model = Category
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         response = []
#         for category in self.object_list.order_by('name'):
#             response.append({
#                 'id': category.id,
#                 'name': category.name
#             })
#
#         return JsonResponse(response, safe=False)
#
#
# class CategoryDetailView(DetailView):
#     model = Category
#     def get(self, request, *args, **kwargs):
#         category = self.get_object()
#         return JsonResponse({
#                 'id': category.id,
#                 'name': category.name
#             })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryCreateView(CreateView):
#     model = Category
#     fields = ['name']
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         category = Category.objects.create(
#             name=data['name']
#         )
#         return JsonResponse({
#                 'id': category.id,
#                 'name': category.name
#             })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryUpdateView(UpdateView):
#     model = Category
#     fields = ['name']
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#
#         self.object.name=data['name']
#
#         self.object.save()
#
#         return JsonResponse({
#                 'id': self.object.id,
#                 'name': self.object.name
#             }, safe=False)
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryDeleteView(DeleteView):
#     model = Category
#     success_url = "/"
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({'status': 'ok'}, status=200)
