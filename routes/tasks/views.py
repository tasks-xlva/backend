from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    queryset = Task.objects.none()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["subject"]
    search_fields = ["name"]
    ordering_fields = ["deadline"]

    def get_queryset(self):
        return Task.objects.filter(subject__group__membership__user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return TaskListRetrieveSerializer
        return TaskSerializer
