from django.test import TestCase
from django.urls import reverse

from .utils import add_two_num
# Create your tests here.

class AddTwoNumsTestCase(TestCase):
    def test_add_two_num(self):
        result = add_two_num(2,3)
        self.assertEqual(result,5)
        # python3 manage.py test shop.tests

class ProductCreateViewTestCase(TestCase):
    def test_create_product(self):
        response = self.client.post(
            reverse("shop:product_create"),{
                'name':"some_name", 'price': 123, 'brand':"some_brand", 'desc':"asdsadasd"
            }
        )
        self.assertRedirects(response, reverse('shop:product_list'))