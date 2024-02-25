from django.contrib import admin
from .models import UserLogin, UserSignup,Image,UserStatus,Userpose,Userbegupdate,Level,Index

admin.site.register(UserLogin)
admin.site.register(UserSignup)
admin.site.register(Image)
admin.site.register(UserStatus)
admin.site.register(Userpose)
admin.site.register(Userbegupdate)
admin.site.register(Level)
admin.site.register(Index)


# Register your models here.
