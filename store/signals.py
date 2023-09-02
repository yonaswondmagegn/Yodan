from django.db.models.signals import pre_save
from .models import Product, CartProduct
from django.dispatch import receiver
from django.db.models import F

@receiver(pre_save, sender=CartProduct)
def update_product_count(sender, instance,**kwargs):
    product = instance.product   
    product.soled_count = product.soled_count+1
    product.save()
