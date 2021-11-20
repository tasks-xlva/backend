from rest_framework import serializers
from .models import Task
from routes.subjects.models import Subject


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    subject_id = serializers.IntegerField()

    class Meta:
        model = Task
        fields = ["id", "name", "description", "subject_id", "attachments", "deadline"]

    def create(self, validated_data):
        subject = Subject.objects.get(pk=validated_data.pop("subject_id"))
        return Task.objects.create(**validated_data, subject=subject)
