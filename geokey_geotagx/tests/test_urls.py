from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from ..views import Import, Viewer


class UrlTest(TestCase):
    def test_import_urls(self):
        self.assertEqual(
            reverse('geokey_geotagx:import', kwargs={'project_id': 1}),
            '/api/geotagx/1/import/'
        )

        resolved = resolve('/api/geotagx/1/import/')
        self.assertEqual(resolved.func.func_name, Import.__name__)
