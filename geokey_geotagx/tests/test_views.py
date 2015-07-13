from json import dumps as json_dumps

from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory

from geokey.contributions.models import Observation
from geokey.projects.tests.model_factories import ProjectF
from geokey.categories.tests.model_factories import CategoryFactory

from ..views import Import
from data import FEATURES


class ImportTest(TestCase):
    def setUp(self):
        p = ProjectF.create()
        CategoryFactory.create(**{'project': p})

    def test_post_with_feature_collection(self):
        factory = APIRequestFactory()
        request = factory.post(
            reverse('geokey_geotagx:import'),
            json_dumps(FEATURES),
            content_type='application/json'
        )
        view = Import.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Observation.objects.count(), 3)
