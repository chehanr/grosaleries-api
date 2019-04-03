from django.contrib import admin

from .models import Category, Price, Product, Seller

# Register your models here.

admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Price)
