from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.none()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(subject__group__users=self.request.user)
