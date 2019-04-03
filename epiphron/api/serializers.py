from django.contrib.auth.models import Group, User
from rest_framework import serializers

from ..core.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk',
                  'name',
                  # 'description',
                  'availability',
                  # 'url',
                  'image_url',
                  'added_datetime',)


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
