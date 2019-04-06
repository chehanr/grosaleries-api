"""epiphron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
# router.register(r'products', api_views.ProductList.as_view())

api_urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/sellers/', api_views.SellerList.as_view()),
    path('api/sellers/item/<int:pk>/', api_views.SellerDetail.as_view()),
    path('api/categories/', api_views.CategoryList.as_view()),
    path('api/categories/item/<int:pk>/', api_views.CategoryDetail.as_view()),
    path('api/products/', api_views.ProductList.as_view()),
    path('api/products/item/<int:pk>/', api_views.ProductDetail.as_view()),
]

urlpatterns.extend(api_urlpatterns)
