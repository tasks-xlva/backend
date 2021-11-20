from routes.subjects.serializers import FlatSubjectSerializer
from routes.users.serializers import UserSerializer
from .models import *
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    subjects = FlatSubjectSerializer(many=True)

    class Meta:
        model = Group
        fields = "__all__"

    def create(self, validated_data):
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


class JoinGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["group", "role"]
        read_only_fields = ["group", "role"]

    def create(self, validated_data):
        group = Group.objects.get(
            uuid=self.context["request"].parser_context.get("kwargs").get("uuid")
        )
        membership = Membership.objects.create(
            group=group, user=self.context["request"].user, role="EDITOR"
        )

        return membership
