import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request):

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append({
                'id': category.id,
                'name': category.name
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        category = Category.objects.create(name=cat_data.get('name'))
        return JsonResponse({
                'id': category.id,
                'name': category.name
            })


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()

        response = []
        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(**ad_data)
        # ad.name = ad_data['name']
        # ad.author = ad_data['author']
        # ad.price = ad_data['price']
        # ad.description = ad_data['description']
        # ad.description = ad_data['description']
        # ad.is_published = ad_data['description']

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
        })


class CategoryDetailView(DetailView):
    model = Category
    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
                'id': category.id,
                'name': category.name
            })


class AdDetailView(DetailView):
    model = Ad
    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
        })