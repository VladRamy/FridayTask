from django.test import TestCase
from django.urls import reverse

class TestMainPage(TestCase):

    def test_main_paige_loads_without_errors(self):
        response = self.client(reverse("main:index"))
        html = response.content.decode("utf8")