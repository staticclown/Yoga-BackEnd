from django.contrib import admin
from .models import UserLogin, UserSignup,Image

admin.site.register(UserLogin)
admin.site.register(UserSignup)
admin.site.register(Image)
# Register your models here.
