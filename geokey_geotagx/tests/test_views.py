from json import dumps as json_dumps

from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory

from geokey.contributions.models import Observation
from geokey.projects.tests.model_factories import ProjectFactory
from geokey.categories.tests.model_factories import CategoryFactory
from geokey.users.models import User
from geokey.users.tests.model_factories import UserFactory

from ..views import Import
from data import FEATURES


class ImportTest(TestCase):
    def setUp(self):
        if not User.objects.filter(display_name='AnonymousUser').exists():
            UserFactory.create(display_name='AnonymousUser')
        self.project = ProjectFactory.create()
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
