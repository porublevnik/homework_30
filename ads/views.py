import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from ads.models import Category, Ad, User
from homework_27 import settings


@method_decorator(csrf_exempt, name='dispatch')
class AdsListView(ListView):
    model = Ad
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        cat = request.GET.get('cat', None)
        if cat:
            self.object_list = self.object_list.filter(Q(category_id=cat))

        text = request.GET.get('text', None)
        if text:
            self.object_list = self.object_list.filter(Q(name__icontains=text))

        location = request.GET.get('location', None)
        if location:
            self.object_list = self.object_list.filter(Q(author__location__name__icontains=location))

        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.object_list = self.object_list.filter(Q(price__gte=price_from))
        if price_to:
            self.object_list = self.object_list.filter(Q(price__lte=price_to))

        paginator = Paginator(self.object_list.order_by('-price', 'id'), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        items = []
        for ad in page_obj:
            items.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author.username,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category': ad.category.name,
                'image': ad.image.url if ad.image else None
            })

        response = {
            'items': items,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }
        return JsonResponse(response, safe=False)


class AdDetailView(DetailView):
    model = Ad
    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author.username,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'category': ad.category.name,
            'image': ad.image.url if ad.image else None
        }, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        author = get_object_or_404(User, pk=data.pop('author_id'))
        category = get_object_or_404(Category, pk=data.pop('category_id'))

        ad = Ad.objects.create(author=author, category=category, **data)
        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author.username,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'category': ad.category.name
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = '__all__'
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if 'name' in data:
            self.object.name = data['name']
        if 'price' in data:
            self.object.price = data['price']
        if 'description' in data:
            self.object.description = data['description']
        if 'category_id' in data:
            category = get_object_or_404(Category, pk=data.pop('category_id'))
            self.object.category = category

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'price': self.object.price,
            'description': self.object.description,
            'category': self.object.category.name,
            'is_published': self.object.is_published
        })

@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class ApUploadImageView(UpdateView):
    model = Ad
    fields = '__all__'
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author.username,
            'price': self.object.price,
            'description': self.object.name,
            'is_published': self.object.is_published,
            'category_id': self.object.category_id,
            'image': self.object.image.url
        }, safe=False)
