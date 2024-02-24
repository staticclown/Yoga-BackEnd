from django.contrib import admin
from .models import UserLogin, UserSignup,Image,UserStatus,Userpose

admin.site.register(UserLogin)
admin.site.register(UserSignup)
admin.site.register(Image)
admin.site.register(UserStatus)
admin.site.register(Userpose)

# Register your models here.
