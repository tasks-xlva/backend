from .models import Subject
from .serializers import SubjectSerializer
from rest_framework import viewsets, permissions


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    paginator = None
