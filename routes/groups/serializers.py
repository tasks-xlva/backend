from routes.subjects.serializers import SubjectSerializer
from .models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "number", "subjects"]
        depth = 1
