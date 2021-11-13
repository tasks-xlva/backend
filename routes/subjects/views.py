from .models import Subject
from .serializers import SubjectSerializer
from rest_framework import viewsets, permissions


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.none()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.filter(group__users=self.request.user)
