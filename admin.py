from django.contrib import admin
from app1.models import Categories,Products,UserRegister
# Register your models here.


admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(UserRegister)