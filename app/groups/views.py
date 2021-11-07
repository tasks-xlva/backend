from .models import Group
from .serializers import GroupSerializer
from rest_framework import viewsets, permissions


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
