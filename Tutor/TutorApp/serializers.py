from rest_framework import serializers

from .models import UserLogin, UserSignup


class UserLogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ["username", "userpassword"]


class UserSignup_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = ["signupname", "signuppassword", "signupdob", "signupemail"]
