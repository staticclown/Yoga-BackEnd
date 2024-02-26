from rest_framework import serializers
from .models import UserLogin, UserSignup,ImageStore,Userpose,UserStatus,Userbegupdate,Level,Index

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
        model = ImageStore
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
        fields = ["update","email"]


class LevelupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ["updatelevel", "email"]


class IndexupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ["updateindex", "email"]
