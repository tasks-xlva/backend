from rest_framework import serializers
from .models import Task
from routes.subjects.models import Subject


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        subject = Subject.objects.get(pk=validated_data.pop("subject_id"))
        return Task.objects.create(**validated_data, subject=subject)
