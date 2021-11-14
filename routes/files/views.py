from rest_framework import viewsets, mixins, permissions
from .serializers import *


class FileViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [permissions.IsAuthenticated]
