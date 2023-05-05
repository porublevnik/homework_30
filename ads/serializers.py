from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from categories.models import Category
from users.models import User
from .models import Ad, Selection


class AdSerializer(ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'

class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        exclude = ['description']

class AdAuthorSerializer(ModelSerializer):
    total_ads = SerializerMethodField()

    def get_total_ads(self, obj):
        return obj.ad_set.count()

    class Meta:
        model = User
        fields = ['username', 'id', 'total_ads']


class AdDetailSerializer(ModelSerializer):
    author = AdAuthorSerializer()
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


#######################

class SelectionSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Selection


class SelectionListSerializer(ModelSerializer):

    class Meta:
        fields = ['id', 'name']
        model = Selection



class SelectionDetailSerializer(ModelSerializer):
    items = AdSerializer(many=True)
    owner = SlugRelatedField(slug_field='username', required=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = Selection



class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field='username', required=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = Selection

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)

