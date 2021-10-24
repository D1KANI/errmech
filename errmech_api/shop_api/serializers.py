from rest_framework import serializers
from .models import Category, Product


class GetCategorySerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id', 'title', 'slug'
        ]


class GetProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
