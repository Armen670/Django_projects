from django.test import TestCase
from django.urls import reverse, reverse_lazy
import json

# Create your tests here.

class GetCookieView(TestCase):
    def test_get_cookie_view(self):
        response = self.client.get(reverse("myauth:cookie-get"))
        self.assertContains(response, 'Cookie value: ')

class FooBarViewTest(TestCase):
    def test_foo_bar_view(self):
        response = self.client.get(reverse_lazy("myauth:foo-bar"))
        self.assertEqual(response.status_code, 200) #проверили что статус-код 200
        self.assertEqual(
            response.headers['content-type'],'application/json' # проверили заголовки
        )
        expected_data = {'foo': 'bar','spam': 'eggs'}
        json_content = json.loads(response.content)
        self.assertEqual(json_content , expected_data)
        #Более простой способ ->
        #self.assertJSONEqual(response.content,expected_data)