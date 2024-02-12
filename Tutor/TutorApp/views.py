from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from rest_framework import generics
from .models import UserLogin, UserSignup
from .serializers import UserLogin_serializer, UserSignup_serializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
import os


class ImageView(APIView):
    def post(self, request, *args, **kwargs):
        # Delete existing images
        Image.objects.all().delete()

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def home(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        frame_data = data.get("frameData")
        # Process the frame data as needed
        print(frame_data)
        return JsonResponse({"status": "success"})


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


class UserSignupView(generics.ListCreateAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignup_serializer
