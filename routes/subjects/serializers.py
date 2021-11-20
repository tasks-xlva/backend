from .models import Subject
from routes.groups.models import Group
from routes.tasks.serializers import TaskSerializer
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = "__all__"

    def create(self, validated_data):
        group = Group.objects.get(pk=validated_data.pop("group_id"))
        return Subject.objects.create(**validated_data, group=group)
