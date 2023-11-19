from django.test import TestCase
from django.urls import reverse

class TestMainPage(TestCase):

    def test_main_paige_loads_without_errors(self):
        response = self.client.get(reverse('main:home'))
        html = response.content.decode("utf8")
        self.assertTrue(html.strip().startswith("<!doctype html>"))
        self.assertTrue(html.strip().endswith("</html>"))
        self.assertTemplateUsed(response, "main/index.html")