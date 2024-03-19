from django.http import HttpResponse
from rest_framework import generics
import torch
import pathlib
import requests
import os
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
    PoseviewSerializer,
)
from .serializers import LevelupdateSerializer, IndexupdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
from django.http import HttpResponse
import os

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


def get_image(request, image_name):
    image_path = os.path.join('path_to_your_image_directory', image_name)
    with open(image_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")  # Adjust content type based on your image type


def skelton():
   
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
        image1 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        results = pose.process(image1)
        # landmarks = results.pose_landmarks.landmark
        if results.pose_landmarks:  # Check if pose_landmarks is not None
            landmarks = results.pose_landmarks.landmark
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
            image1,
            str(angle),
            tuple(np.multiply(elbow, [image.shape[1], image.shape[0]]).astype(int)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
            )
            cv2.putText(
            image1,
            str(angle1),
            tuple(np.multiply(elbow1, [image.shape[1], image.shape[0]]).astype(int)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
            )
            cv2.putText(
            image1,
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
            image1,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
            )
        # Continue with your code that uses landmarks
        else:
        # Handle the case where pose_landmarks is None
            print("No pose landmarks detected")

        # Get coordinates
        

        # Display the image
        # cv2.imshow("Mediapipe Feed", image1)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        print(type(image1))
        model = torch.hub.load('yolov5', 'custom', path='yolov5/best3.pt', source='local',force_reload=True)
        model.conf = 0.1  # local repo
        im = 'yolov5/q.jpg'  # file, Path, PIL.Image, OpenCV, nparray, list
        print(type(im))
        results = model(image)  # inference
        results.save()


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
        
        def delete_directory_contents(directory):
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)

            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                delete_directory_contents(file_path)
            os.rmdir(file_path)


        ImageStore.objects.all().delete()


class ImageView(generics.CreateAPIView):
    serializer_class = PoseviewSerializer
    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        pose = requestbody["poseName"]
        obj = Userpose.objects.get(poseName=pose)
        image_path=obj.img.path
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/*")


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
