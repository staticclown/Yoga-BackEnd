from django.db import models


class UserLogin(models.Model):
    useremail = models.CharField(max_length=30)
    userpassword = models.CharField(max_length=30)


class UserSignup(models.Model):
    signupname = models.CharField(max_length=30)
    signuppassword = models.CharField(max_length=30)
    signupdob = models.CharField(max_length=30)
    signupemail = models.CharField(max_length=30, primary_key=True)


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
