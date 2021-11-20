from rest_framework import serializers
from .models import Task
from routes.subjects.models import Subject


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
