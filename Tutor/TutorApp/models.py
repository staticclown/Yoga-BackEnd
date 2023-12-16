from django.db import models

class UserLogin(models.Model):
    username=models.CharField(max_length=30)
    userpassword=models.CharField(max_length=30)

