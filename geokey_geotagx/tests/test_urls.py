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
        self.assertEqual(resolved.kwargs['project_id'], '1')

    def test_viewer_urls(self):
        self.assertEqual(
            reverse('geokey_geotagx:viewer', kwargs={'project_id': 1}),
            '/geotagx/1/'
        )

        resolved = resolve('/geotagx/1/')
        self.assertEqual(resolved.func.func_name, Viewer.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
