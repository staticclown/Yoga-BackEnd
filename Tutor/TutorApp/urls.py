from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.UserLoginView.as_view()),
    path("signup/",views.UserSignupView.as_view()),
    path("image/",views.ImageView.as_view()),
    path("video", views.home),
]
