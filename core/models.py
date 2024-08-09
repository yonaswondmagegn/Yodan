from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class CustomUserManager(UserManager):

    

    def create_custom_user(self, phonenumber,password=None, **extra_fields):
        if not phonenumber:
            return ValueError('Phone Number is Requred')
        if extra_fields.get('is_superuser'):
            print('true ......****')
            extra_fields.setdefault('is_active',True)
             
        extra_fields.setdefault('is_active',False)
        user = self.model(phonenumber = phonenumber,**extra_fields)
        if password:
            user.set_password(password)
        else:
             user.set_password('default_password_for_authentication')
        user.save(using = self._db)
        return user
    
    def create_user(self, phonenumber,password=None,**extra_fields):
          extra_fields.setdefault("is_staff", False)
          extra_fields.setdefault("is_superuser", False)
          return self.create_custom_user(phonenumber,password,**extra_fields)
    
    
    def create_superuser(self,phonenumber,password=None, **extra_fields):
          extra_fields.setdefault("is_staff", True)
          extra_fields.setdefault("is_superuser", True)
          return self.create_custom_user(phonenumber,password ,**extra_fields)



class User(AbstractUser):
    phonenumber = models.CharField(unique=True,max_length=13)
    username = models.CharField(null=True,unique=False,blank=True,max_length=225)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []

class AuthVerification(models.Model):
     unique_id = models.TextField() 
     code = models.IntegerField()
     user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
     is_verified = models.BooleanField(default=False)
     is_expired = models.BooleanField(default=False)
     is_used = models.BooleanField(default=False)
     date = models.DateTimeField(default= timezone.now)



     
     

