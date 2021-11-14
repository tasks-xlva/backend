from routes.subjects.serializers import SubjectSerializer
from routes.users.serializers import UserSerializer
from .models import *
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "number", "subjects"]
        depth = 1


class GroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"
