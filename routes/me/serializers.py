from routes.users.models import User
from rest_framework import serializers


class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
