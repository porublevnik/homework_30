import json

from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from users.models import User, Location
from homework_27 import settings

method_decorator(csrf_exempt, name='dispatch')
class UsersListView(ListView):
    queryset = User.objects.annotate(total_ads=Count('ad', filter=Q(ad__is_published=True)))
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list.order_by('username'), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        items = []
        for user in page_obj:
            items.append({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'password': user.password,
                'role': user.role,
                'age': user.age,
                'locations': list(map(str, user.locations.all())),
                'total_ads': user.total_ads
            })

        response = {
            'items': items,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }
        return JsonResponse(response, safe=False)


class UserDetailView(DetailView):
    model = User
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': user.password,
            'role': user.role,
            'age': user.age,
            'locations': list(map(str, user.locations.all()))
        }, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        locations = data.pop('locations')
        user = User.objects.create(**data)
        for loc_name in locations:
            loc, created = Location.objects.get_or_create(name=loc_name)
            user.locations.add(loc)
        user.save()

        return JsonResponse({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': user.password,
            'role': user.role,
            'age': user.age,
            'locations': [loc.name for loc in user.locations.all()]
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if 'first_name' in data:
            self.object.first_name = data['first_name']
        if 'last_name' in data:
            self.object.last_name = data['last_name']
        if 'username' in data:
            self.object.username = data['username']
        if 'age' in data:
            self.object.age = data['age']
        if 'locations' in data:
            self.object.locations.clear()
            for loc_name in data["locations"]:
                loc, created = Location.objects.get_or_create(name=loc_name)
                self.object.locations.add(loc)

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'username': self.object.username,
            'password': self.object.password,
            'role': self.object.role,
            'age': self.object.age,
            'locations': [loc.name for loc in self.object.locations.all()]
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)
