from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phonenumber = models.IntegerField(blank=False,null=True,unique=True)
    # username = models.CharField(max_length=250,unique=False)


