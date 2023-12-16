from rest_framework import serializers

from .models import UserLogin


class UserLogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ["username", "userpassword"]
