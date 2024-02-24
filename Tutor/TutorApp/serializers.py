from rest_framework import serializers
from .models import UserLogin, UserSignup,Image,Userpose,UserStatus,Userbegupdate

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


class UserposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userpose
        fields = [
            " pose_id",
            "lock",
            "description",
            "img",
            "level",
            "index_no",
            "poseName",
        ]


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = [" beginner", "index", "mail_id", "level"]


class UserbegupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userbegupdate
        fields = [" beg","email"]
