from rest_framework import viewsets, mixins, permissions
from .serializers import *


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
