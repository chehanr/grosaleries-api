from django.contrib import admin

from .models import Category, Product, Seller

# Register your models here.

admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
