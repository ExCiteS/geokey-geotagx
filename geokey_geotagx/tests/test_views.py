from json import dumps as json_dumps

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.contrib.auth.models import AnonymousUser
from django.template.loader import render_to_string

from rest_framework.test import APIRequestFactory

from geokey.contributions.models import Observation
from geokey.projects.tests.model_factories import ProjectF
from geokey.categories.tests.model_factories import CategoryFactory

from ..views import Import, Viewer
from data import FEATURES


class ImportTest(TestCase):
    def setUp(self):
        self.project = ProjectF.create()
        CategoryFactory.create(**{'project': self.project, 'name': 'Result'})

    def test_post_with_feature_collection(self):
        factory = APIRequestFactory()
        request = factory.post(
            reverse('geokey_geotagx:import', kwargs={'project_id': 1}),
            json_dumps(FEATURES),
            content_type='application/json'
        )
        view = Import.as_view()
        response = view(request, project_id=self.project.id)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Observation.objects.count(), 3)
