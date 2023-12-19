from django.contrib import admin
from .models import UserLogin, UserSignup

admin.site.register(UserLogin)
admin.site.register(UserSignup)
# Register your models here.
