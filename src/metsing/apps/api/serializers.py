from rest_framework import serializers

from metsing import models


class UserProfileSerializer(serializers.ModelSerializer):
    """
    View to display User profile.
    """
    class Meta:
        model = models.User
        fields = ('id', 'mobile_number', 'full_name')
