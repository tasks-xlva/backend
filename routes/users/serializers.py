from djoser import serializers


class UserSerializer(serializers.UserSerializer):
    class Meta(serializers.UserSerializer.Meta):
        extra_kwargs = {"password": {"write_only": True}}
