from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from ..views import Import


class UrlTest(TestCase):
    def test_import_urls(self):
        self.assertEqual(
            reverse('geokey_geotagx:import'),
            '/api/geotagx/import/'
        )

        resolved = resolve('/api/geotagx/import/')
        self.assertEqual(resolved.func.func_name, Import.__name__)
