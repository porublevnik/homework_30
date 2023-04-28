from rest_framework import serializers
from models import Ad, Category


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = '__all__'