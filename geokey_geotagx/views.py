from json import dumps as json_dumps

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from geokey.users.models import User
from geokey.contributions.serializers import ContributionSerializer
from geokey.projects.models import Project
from geokey.categories.models import Category

import settings


class Import(APIView):
    def store_feature(self, feature):
        user = User.objects.get(display_name='AnonymousUser')

        feature['meta'] = {
            'category': self.category.id
        }
        feature['location'] = {
            'geometry': json_dumps(feature.pop('geometry'))
        }

        serializer = ContributionSerializer(
            data=feature,
            context={'user': user, 'project': self.project}
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    def post(self, request):
        self.project = Project.objects.get(pk=settings.project)
        self.category = Category.objects.get(pk=settings.category)

        data = request.DATA

        if data['type'] == 'FeatureCollection':
            for feature in data['features']:
                self.store_feature(feature)

            return Response('Objects created', status=status.HTTP_201_CREATED)
