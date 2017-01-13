from rest_framework import viewsets

from metsing.apps.api.serializers import UserProfileSerializer
from metsing.models import User


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
