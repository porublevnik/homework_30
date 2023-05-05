import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad, User, Selection
from ads.permissions import IsOwner, IsStaff
from ads.serializers import AdSerializer, SelectionSerializer, AdListSerializer, AdDetailSerializer, \
    SelectionListSerializer, SelectionDetailSerializer, SelectionCreateSerializer
from homework_27 import settings


class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.all()

    serializers = {
        'list': AdListSerializer,
        'retrieve': AdDetailSerializer,
    }
    default_serializer = AdSerializer

    permissions = {
        'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner | IsStaff],
        'partial_update': [IsAuthenticated, IsOwner | IsStaff],
        'destroy': [IsAuthenticated, IsOwner | IsStaff]
    }
    default_permission = [AllowAny]
    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get(self, request, *args, **kwargs):

        cat = request.GET.get('cat', None)
        if cat:
            self.queryset = self.queryset.filter(Q(category_id=cat))

        text = request.GET.get('text', None)
        if text:
            self.queryset = self.queryset.filter(Q(name__icontains=text))

        location = request.GET.get('location', None)
        authors = User.objects.all()
        if location:
            authors = authors.filter(Q(locations__name__icontains=location))
            self.queryset = self.queryset.filter(Q(author__in=authors))

        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(Q(price__gte=price_from))
        if price_to:
            self.queryset = self.queryset.filter(Q(price__lte=price_to))


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


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    default_serializer = SelectionSerializer
    serializers = {
        'list': SelectionListSerializer,
        'retrieve': SelectionDetailSerializer,
        'create': SelectionCreateSerializer
    }

    permissions = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner],
        'partial_update': [IsAuthenticated, IsOwner],
        'destroy': [IsAuthenticated, IsOwner]
    }
    default_permission = [AllowAny]

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)