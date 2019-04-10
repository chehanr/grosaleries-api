from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from ..core.models import Category, Product, Seller


class APITestCase(TestCase):

    """
    Core API tests.
    """

    def setUp(self):
        self.client = APIClient()

        self.seller = Seller()
        self.seller = Seller(name="TestSeller")
        self.seller.save()

        self.category = Category()
        self.category = Category(name="TestCategory")
        self.category.save()

        self.product = Product()
        self.product = Product(seller=self.seller,
                               category=self.category,
                               name="TestProduct")
        self.product.save()

    def test_can_get_seller_list(self):
        """GET /sellers returns a list of sellers."""
        url = reverse('api-seller-list')
        response = self.client.get(url)
        assert response.status_code == 200, "Expect 200 OK. got: {}".format(
            response.status_code)

    def test_can_get_seller_item(self):
        """GET /sellers/item/{pk} returns a seller."""
        url = reverse('api-seller-item', args=[self.seller.pk])
        response = self.client.get(url)
        assert response.status_code == 200, "Expect 200 OK. got: {}".format(
            response.status_code)

    def test_can_get_category_list(self):
        """GET /categories returns a list of categories."""
        url = reverse('api-category-list')
        response = self.client.get(url)
        assert response.status_code == 200, "Expect 200 OK. got: {}".format(
            response.status_code)

    def test_can_get_category_item(self):
        """GET /categories/item/{pk} returns a category."""
        url = reverse('api-category-item', args=[self.category.pk])
        response = self.client.get(url)
        assert response.status_code == 200, "Expect 200 OK. got: {}".format(
            response.status_code)

    def test_can_get_product_list(self):
        """GET /products returns a list of products."""
        url = reverse('api-product-list')
        response = self.client.get(url)
        assert response.status_code == 200, "Expect 200 OK. got: {}".format(
            response.status_code)

    def test_can_get_product_item(self):
        """GET /products/item/{pk} returns a product."""
        url = reverse('api-product-item', args=[self.product.pk])
        response = self.client.get(url)
        assert response.status_code == 200, "Expect 200 OK. got: {}".format(
            response.status_code)

    def tearDown(self):
        for seller in Seller.objects.all():
            seller.delete()
        for category in Category.objects.all():
            category.delete()
        for product in Product.objects.all():
            product.delete()
