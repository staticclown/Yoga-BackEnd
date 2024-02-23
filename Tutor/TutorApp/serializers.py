from rest_framework import serializers

from .models import UserLogin, UserSignup,Image


class UserLogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ["useremail", "userpassword"]


class UserSignup_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = ["signupname", "signuppassword", "signupdob", "signupemail"]




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [ "image"]
        
