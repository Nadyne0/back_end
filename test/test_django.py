from django.test import TestCase
from django.urls import reverse


import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Projeto.settings")


class URLsTest(TestCase):
    def test_nada(self):
        assert 1 == 1


def test_poema_lista_url_ok(self):
    url = reverse("poesias:poema_lista")
    self.assertEqual(url, "poema_lista/")
