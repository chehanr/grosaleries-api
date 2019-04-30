from django.contrib.auth.models import Group, User
from rest_framework import serializers

from ..core.models import Category, Product, Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name',)


class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id',
                  'name',
                  'description',
                  'url',
                  'added_datetime',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'description',
                  'added_datetime',)


class ProductSerializer(serializers.ModelSerializer):
    category = SellerSerializer()
    seller = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'price',
                #   'quantity',
                  'availability',
                  'url',
                  'image_url',
                  'added_datetime',
                  'seller',
                  'category',)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = SellerSerializer()
    seller = CategorySerializer()

    class Meta:
        model = Product
        fields = ('pk',
                  'name',
                  'description',
                  'price',
                #   'quantity',
                  'extra_data',
                  'availability',
                  'url',
                  'image_url',
                  'added_datetime',
                  'seller',
                  'category',)
