from .models import Subject
from routes.tasks.serializers import TaskSerializer
from rest_framework import serializers


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "name", "description", "tasks"]
