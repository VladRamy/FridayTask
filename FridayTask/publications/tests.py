import pytest as pytest
from django.test import TestCase
from publications.models import Publications
from mixer.backend.django import mixer


class TestPublications(TestCase):

    def test_index(self):
        response = self.client.get('/publications/')
        self.assertEqual(response.status_code, 200)

    def test_publication_can_be_created(self):
        publication = mixer.blend(
            Publications,
            title="вмвмвм",
            full_text="мввмымфыфсы",
            html="<b>html here...</b>",
        )
        assert Publications.objects.count() == 1
        assert publication.title == "вмвмвм"

