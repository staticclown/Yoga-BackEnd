from django.contrib import admin
from .models import UserLogin, UserSignup,ImageStore,UserStatus,Userpose,Userbegupdate,Level,Index,TempImagestore

admin.site.register(UserLogin)
admin.site.register(UserSignup)
admin.site.register(ImageStore)
admin.site.register(UserStatus)
admin.site.register(Userpose)
admin.site.register(Userbegupdate)
admin.site.register(Level)
admin.site.register(Index)
admin.site.register(TempImagestore)

# Register your models here.
