from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'вы не являетесь владельцем данной подборки!'

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            owner = obj.owner
        elif hasattr(obj, 'author'):
            owner = obj.author
        else:
            raise Exception('Неверно применен permission')

        if request.user == owner:
            return True


class IsStaff(BasePermission):
    message = 'вы не являетесь модератором или администратором!'

    def has_object_permission(self, request, view, obj):
        if request.user.role in ['moderator', 'admin']:
            return True
