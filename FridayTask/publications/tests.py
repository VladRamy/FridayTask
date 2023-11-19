import pytest as pytest
from django.test import TestCase
from publications.models import Publications
from mixer.backend.django import mixer
from django.urls import reverse
from .forms import PublicationsForm

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

    def test_publication_create_by_form(self):
        data = {
            'title': "Влад",
            'full_text': 'Владислав',
            'anons': "Влад",
            'date': '2003-02-22'
        }

        form = PublicationsForm(data)
        assert form.is_valid() == True
        form.save()

        assert Publications.objects.count() == 1

    def test_delete_publication(self):
        publication = mixer.blend(
            Publications,
            title="вмвмвм",
            full_text="мввмымфыфсы",
            html="<b>html here...</b>",
        )

        assert Publications.objects.count() == 1

        self.client.post(reverse('publ-delete', kwargs={'pk': publication.id}))

        assert Publications.objects.count() == 0

