from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Seller(models.Model):
    """
    Seller model.
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    added_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Seller")
        verbose_name_plural = _("Sellers")

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category model.
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    added_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model.

    # TODO add filepath field for image.
    """

    seller = models.ForeignKey(
        Seller, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=128)
    # price = models.FloatField()
    description = models.CharField(max_length=512, blank=True, null=True)
    quantity = models.CharField(max_length=64, blank=True, null=True)
    extra_data = JSONField(blank=True, null=True)
    availability = models.BooleanField(default=True)
    url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    added_datetime = models.DateTimeField(auto_now_add=True)
    # modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Price(models.Model):
    """
    Price model.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_datetime = models.DateTimeField(auto_now_add=True)
    recorded_datetime = models.DateField()
    price = models.FloatField()

    class Meta:
        verbose_name = _("Price")
        verbose_name_plural = _("Prices")

    def __str__(self):
        return '{0} - {1}'.format(self.product.name, self.price)
