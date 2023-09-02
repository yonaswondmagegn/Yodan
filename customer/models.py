from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Customer(models.Model):
    sex = (("M","Male"),
              ("F","Female"),
              ("NR","NOT REGISTERED"))
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customers_pics',default='default.png')
    sex = models.CharField(max_length=2,choices=sex,default='NR')
    date = models.DateTimeField(default=timezone.now)



