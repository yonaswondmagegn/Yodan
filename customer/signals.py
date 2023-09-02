from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from django.conf import settings

User = settings.AUTH_USER_MODEL
@receiver(post_save,sender = User)
def createCustomer(sender,created,instance,**kwargs):
    if created:
        Customer.objects.create(user = instance)

