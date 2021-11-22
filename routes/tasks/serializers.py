from rest_framework import serializers
from .models import Task
from routes.files.serializers import FileSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskListRetrieveSerializer(serializers.ModelSerializer):
    attachments = FileSerializer(many=True, allow_null=True)

    class Meta:
        model = Task
        fields = "__all__"
