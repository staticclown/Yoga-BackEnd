from django.db import models


class UserLogin(models.Model):
    useremail = models.CharField(max_length=30)
    userpassword = models.CharField(max_length=30)


class UserSignup(models.Model):
    signupname = models.CharField(max_length=30)
    signuppassword = models.CharField(max_length=30)
    signupdob = models.CharField(max_length=30)
    signupemail = models.CharField(max_length=30, primary_key=True)


class ImageStore(models.Model):
    image = models.ImageField(upload_to="Userimages/",max_length=30000)


class TempImagestore(models.Model):
    image = models.ImageField(upload_to="tempimages/", max_length=30000)


class UserStatus(models.Model):

    beginner=models.IntegerField()
    level=models.IntegerField()
    mail_id=models.CharField(max_length=50,primary_key=True)
    index=models.IntegerField()

class Userpose(models.Model):
    poseName=models.CharField(max_length=40)
    index_no=models.IntegerField()
    level=models.IntegerField()
    img=models.ImageField(upload_to="Poseimages/",max_length=30000)
    description=models.CharField(max_length=5000)

class Userbegupdate(models.Model):
    update = models.IntegerField()
    email = models.CharField(max_length=30)

class Level(models.Model):
    updatelevel=models.IntegerField()
    email = models.CharField(max_length=30)


class Index(models.Model):
    updateindex=models.IntegerField()
    email = models.CharField(max_length=30)
