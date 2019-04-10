from django.test import TestCase

from ..core.models import Category, Product, Seller


class APITestCase(TestCase):

    """
    Core API tests.
    TODO Implement.
    """

    def setUp(self):
        self.seller = Seller()
        self.category = Category()
        self.product = Product()

    def test_can_get_seller_list(self):
        """GET /sellers returns a list of sellers."""
        assert False is True

    def test_can_get_seller_item(self):
        """GET /sellers/item/{pk} returns a seller."""
        assert False is True

    def test_can_get_category_list(self):
        """GET /categories returns a list of categories."""
        assert False is True

    def test_can_get_category_item(self):
        """GET /categories/item/{pk} returns a category."""
        assert False is True

    def test_can_get_product_list(self):
        """GET /products returns a list of products."""
        assert False is True

    def test_can_get_product_item(self):
        """GET /products/item/{pk} returns a product."""
        assert False is True
