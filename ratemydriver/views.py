import logging

from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response

from ratemydriver.serializers import UserSerializer
from ratemydriver.models import RMDUser


logger = logging.Logger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = RMDUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]