from django.http import HttpResponse
from rest_framework import generics
import requests
from .models import (
    UserLogin,
    UserSignup,
    ImageStore,
    Userbegupdate,
    UserStatus,
    Level,
    Index,
    TempImagestore,
    Userpose,
)
from .serializers import (
    UserLogin_serializer,
    UserSignup_serializer,
    ImageSerializer,
    UserbegupdateSerializer,
    UserposeSerializer,
    UserStatusSerializer,
)
from .serializers import LevelupdateSerializer, IndexupdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
import os
import shutil

def skelton():
    # image_object = ImageStore.objects.first()

    # image_url = image_object.image.url
    # base_url = 'http://192.168.1.100:8000\Yoga-BackEnd\Tutor'  # Replace with your Django server's base URL
    # absolute_image_url = f'{base_url}{image_url}'
    # image_url=absolute_image_url
    # print(image_url)
    # response = requests.get(image_url)
    # print(response.status_code)
    # if response.status_code == 200:
    #     new_image_instance = TempImagestore()
    #     print("inside")
    #     new_image_instance.image.save(image_object.image.name, ContentFile(response.content), save=True)
    #     new_image_instance.save()

    def calculate_angle(a,b,c):
        a = np.array(a) # First
        b = np.array(b) # Mid
        c = np.array(c) # End

        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)

        if angle >180.0:
            angle = 360-angle

        return angle 
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    # Load the image
    # image_path = image_store_instance.image
    image_store_instance = ImageStore.objects.first()
    image_path = image_store_instance.image.path
    print("Image path:", image_path)
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Recolor image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        results = pose.process(image)
        landmarks = results.pose_landmarks.landmark

        # Get coordinates
        shoulder = [
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
        ]
        elbow = [
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
        ]
        wrist = [
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
        ]
        shoulder1 = [
            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y,
        ]
        elbow1 = [
            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y,
        ]
        wrist1 = [
            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y,
        ]
        hip1 = [
            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
        ]
        knee1 = [
            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
        ]
        ankle1 = [
            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
        ]

        # Calculate angles
        angle = calculate_angle(shoulder, elbow, wrist)
        angle1 = calculate_angle(shoulder1, elbow1, wrist1)
        angle2 = calculate_angle(hip1, knee1, ankle1)

        # Visualize angles
        cv2.putText(
            image,
            str(angle),
            tuple(np.multiply(elbow, [image.shape[1], image.shape[0]]).astype(int)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )
        cv2.putText(
            image,
            str(angle1),
            tuple(np.multiply(elbow1, [image.shape[1], image.shape[0]]).astype(int)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )
        cv2.putText(
            image,
            str(angle2),
            tuple(np.multiply(knee1, [image.shape[1], image.shape[0]]).astype(int)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        # Render detections
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
        )

        # Display the image
        # cv2.imshow("Mediapipe Feed", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        image_store_instance.save()


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


class UserposeUpdate(generics.ListCreateAPIView):
    queryset = Userpose.objects.all()
    serializer_class = UserposeSerializer


class UserStatus(generics.RetrieveUpdateAPIView):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer


class UserDetails(generics.RetrieveUpdateAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignup_serializer
