from routes.subjects.serializers import SubjectSerializer
from .models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ["id", "number", "subjects"]
