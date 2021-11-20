from routes.subjects.serializers import SubjectSerializer
from routes.users.serializers import UserSerializer
from .models import *
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "number", "subjects"]
        depth = 1

    def create(self, validated_data):
        print(validated_data)
        group = Group.objects.create(**validated_data)
        Membership.objects.create(
            group=group, user=self.context["request"].user, role="EDITOR"
        )

        return group


class GroupMembershipSerializer(serializers.ModelSerializer):
    group = serializers.IntegerField(write_only=True)
    user = UserSerializer()

    class Meta:
        model = Membership
        fields = "__all__"
