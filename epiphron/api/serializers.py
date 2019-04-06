from django.contrib.auth.models import Group, User
from rest_framework import serializers

from ..core.models import Category, Product, Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    category = SellerSerializer()
    seller = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'quantity',
                  'availability',
                  'url',
                  'image_url',
                  'added_datetime',
                  'seller',
                  'category',)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk',
                  'name',
                  'description',
                  'quantity',
                  'extra_data',
                  'availability',
                  'url',
                  'image_url',
                  'added_datetime',
                  'seller',
                  'category',)
