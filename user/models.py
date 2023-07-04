from django.db import models                       
from django.contrib.auth.models import AbstractUser,BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,password=None, is_staff = False, is_superuser = False):
        if not email:
            raise ValueError("u must have an email")
        if not first_name:
             raise ValueError("u must have an first name")
        if not last_name:
             raise ValueError("u must have an last name")
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
    def create_superuser(self,email, first_name, last_name,password=None):
        user = self.create_user( email = email, first_name = first_name, last_name = last_name,password=password, is_staff=True, is_superuser=True)
        user.save()
        return user
            
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    password =models.CharField(max_length=100)
    username = None
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "first_name", "last_name"]
    
