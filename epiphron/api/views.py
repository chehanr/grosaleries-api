from django.contrib.auth.models import Group, User
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters, generics, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from ..core.models import Category, Product, Seller
from .serializers import (CategoryDetailSerializer, CategorySerializer,
                          ProductDetailSerializer, ProductSerializer,
                          SellerDetailSerializer, SellerSerializer)


class SellerList(generics.ListAPIView):
    """
    List all sellers.
    """

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    ordering = ('pk',)


class SellerDetail(APIView):
    """
    Retrieve a single seller instance.
    """

    def get_object(self, pk):
        try:
            return Seller.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        seller = self.get_object(pk)
        serializer = SellerDetailSerializer(seller)
        return Response(serializer.data)


class CategoryList(generics.ListAPIView):
    """
    List all categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering = ('pk',)


class CategoryDetail(APIView):
    """
    Retrieve a single category instance.
    """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)


class ProductList(generics.ListAPIView):
    """
    List all products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name',)
    ordering_fields = ('pk', 'availability', 'added_datetime', 'price',)
    ordering = ('pk',)

    def get_queryset(self):
        queryset = Product.objects.all()
        qp_availability = self.request.query_params.get('availability')
        qp_category = self.request.query_params.get('category')
        qp_price = self.request.query_params.get('price')
        qp_seller = self.request.query_params.get('seller')

        if qp_availability:
            queryset = queryset.filter(availability=qp_availability)
        if qp_seller:
            if qp_seller.isdigit():
                queryset = queryset.filter(seller=qp_seller)
            else:
                queryset = queryset.filter(seller__name__iexact=qp_seller)
                
        return queryset


class ProductDetail(APIView):
    """
    Retrieve a single product instance.
    """

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
