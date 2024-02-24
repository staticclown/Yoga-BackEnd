from django.http import HttpResponse
from rest_framework import generics
from .models import UserLogin, UserSignup,Image,Userbegupdate,UserStatus
from .serializers import UserLogin_serializer, UserSignup_serializer,ImageSerializer,UserbegupdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ImageEntry(APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDelete(APIView):

    def post(self, request, *args, **kwargs):
        Image.objects.all().delete()


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

        obj=UserSignup.objects.all()

        for i in obj:
            if i.signupemail==tempmail:
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
        tempname = requestbody["beg"]
        obj = UserStatus.objects.get(tid=title)
        obj.beginner=beg
        obj.save()