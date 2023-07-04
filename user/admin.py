from django.contrib import admin
from .models import *
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'email', 'username', 'first_name', 'last_name' ]
    
# admin.site.register(User)



admin.site.register(User)
