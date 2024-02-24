from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.UserLoginView.as_view()),
    path("signup/", views.UserSignupView.as_view()),
    path("image/", views.ImageEntry.as_view()),
    path("imgdelete/", views.ImageDelete.as_view()),
    path("userupdate/", views.UserUpdate.as_view()),
    path("imageview/", views.Imageview.as_view()),
]
