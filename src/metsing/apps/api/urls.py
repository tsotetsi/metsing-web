from django.conf.urls import url, include
from rest_framework import routers

from metsing.apps.api.views import UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'profile', UserProfileViewSet, base_name='user-profile')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
