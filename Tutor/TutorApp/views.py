from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from rest_framework import generics
from .models import UserLogin, UserSignup
from .serializers import UserLogin_serializer, UserSignup_serializer
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse("hi")


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
