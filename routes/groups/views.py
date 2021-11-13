from .models import Group
from .serializers import *
from rest_framework import viewsets, permissions


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.none()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Group.objects.filter(users=self.request.user)
