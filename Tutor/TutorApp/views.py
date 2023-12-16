from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from rest_framework import generics
from .models import UserLogin
from .serializers import UserLogin_serializer


def home(request):
    return HttpResponse("hi")


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLogin_serializer
    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)

        # word = requestbody["password"]
        # if word == "1234":
        #     return Response("SUCCESS", status=status.HTTP_200_OK)
        # else:
        #     return Response("NO", status=status.HTTP_200_OK)
    
