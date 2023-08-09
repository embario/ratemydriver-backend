from rest_framework import serializers

from ratemydriver.models import RMDUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField(source='auth_token.key')

    class Meta:
        model = RMDUser
        fields = ['url', 'username', 'email', 'groups', 'is_active', 'token']
