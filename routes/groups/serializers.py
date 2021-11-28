from routes.subjects.serializers import FlatSubjectSerializer
from routes.users.serializers import UserSerializer
from .models import *
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    subjects = FlatSubjectSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Group
        fields = "__all__"

    def create(self, validated_data):
        group = Group.objects.create(**validated_data)
        Membership.objects.create(
            group=group, user=self.context["request"].user, role="ADMIN"
        )

        return group


class GroupMembershipSerializer(serializers.ModelSerializer):
    group = serializers.IntegerField(write_only=True)
    user = UserSerializer()

    class Meta:
        model = Membership
        fields = "__all__"


class JoinGroupSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(write_only=True)

    class Meta:
        model = Membership
        fields = ["group", "role", "uuid"]
        read_only_fields = ["group", "role"]

    def create(self, validated_data):
        group = Group.objects.get(uuid=validated_data["uuid"])
        membership = Membership.objects.create(
            group=group, user=self.context["request"].user, role="EDITOR"
        )

        return membership
