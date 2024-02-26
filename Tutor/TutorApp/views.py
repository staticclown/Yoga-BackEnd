from django.http import HttpResponse
from rest_framework import generics
from .models import (
    UserLogin,
    UserSignup,
    ImageStore,
    Userbegupdate,
    UserStatus,
    Level,
    Index,
)
from .serializers import (
    UserLogin_serializer,
    UserSignup_serializer,
    ImageSerializer,
    UserbegupdateSerializer,
)
from .serializers import LevelupdateSerializer, IndexupdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image


def skelton():
    image_object = ImageStore.objects.get(pk=1) 
    image_url = image_object.image.url


class ImageEntry(APIView):
    def post(self, request, *args, **kwargs):

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            skelton()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDelete(APIView):

    def post(self, request, *args, **kwargs):
        ImageStore.objects.all().delete()


class ImageView(generics.ListCreateAPIView):
    queryset = ImageStore.objects.all()
    serializer_class = ImageSerializer


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLogin_serializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)

        word = requestbody["userpassword"]
        mail = requestbody["useremail"]
        try:
            obj = UserSignup.objects.get(signupemail=mail)
            a1 = obj.signuppassword
            print(a1)
            if word == a1:
                return Response("SUCCESS", status=status.HTTP_200_OK)
            else:
                return Response("NO", status=status.HTTP_200_OK)
        except:
            return Response("NO", status=status.HTTP_200_OK)


class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignup_serializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        tempmail = requestbody["signupemail"]
        tempname = requestbody["signupname"]
        tempdob = requestbody["signupdob"]
        temppass = requestbody["signuppassword"]

        obj = UserSignup.objects.all()

        for i in obj:
            if i.signupemail == tempmail:
                return Response("NO", status=status.HTTP_200_OK)

        newEntry = UserSignup(
            signupname=tempname,
            signuppassword=temppass,
            signupdob=tempdob,
            signupemail=tempmail,
        )
        newEntry.save()

        newEntry = UserStatus(
            index=0,
            mail_id=tempmail,
            level=0,
            beginner=1,
        )
        newEntry.save()

        return Response("SUCCESS", status=status.HTTP_200_OK)


class UserUpdate(generics.CreateAPIView):
    serializer_class = UserbegupdateSerializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        tempmail = requestbody["email"]
        tempbeg = requestbody["update"]
        obj = UserStatus.objects.get(mail_id=tempmail)
        obj.beginner = tempbeg
        obj.save()
        return Response("SUCCESS", status=status.HTTP_200_OK)


class LevelUpdate(generics.CreateAPIView):
    serializer_class = LevelupdateSerializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        tempmail = requestbody["email"]
        templevel = requestbody["updatelevel"]
        obj = UserStatus.objects.get(mail_id=tempmail)
        obj.level = templevel
        obj.save()
        return Response("SUCCESS", status=status.HTTP_200_OK)


class IndexUpdate(generics.CreateAPIView):
    serializer_class = IndexupdateSerializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        tempmail = requestbody["email"]
        tempindex = requestbody["updateindex"]
        obj = UserStatus.objects.get(mail_id=tempmail)
        obj.index = tempindex
        obj.save()
        return Response("SUCCESS", status=status.HTTP_200_OK)
