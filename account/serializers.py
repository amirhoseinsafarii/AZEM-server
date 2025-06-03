from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    # verifyPassword = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "phoneNumber",
            "firstName",
            "lastName",
            "teamName",
        ]

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.save()
        return user

    # def validate(self, data):
    #     if data["password"] != data["verifyPassword"]:
    #         raise serializers.ValidationError("password must be mach")
    #     return data
