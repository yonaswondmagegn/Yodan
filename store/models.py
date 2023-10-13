from django.db import models
from django.utils import timezone
from customer.models import Customer


class Image(models.Model):
    image = models.ImageField(upload_to='products_pics')

class Chategory(models.Model):
    title = models.CharField(max_length=225)
    likedrating = models.IntegerField(default=0)
    relatedproducts = models.IntegerField(default=0)


    def realatedproductscount(self):
        chategory_products = Product.objects.filter(chategory = self).count()
        self.relatedproducts = chategory_products
        self.save()
        

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=225)
    images = models.ManyToManyField(Image,related_name='images')
    description = models.TextField()
    price = models.FloatField()
    down_price = models.FloatField(null=True,blank=True)
    chategory = models.ForeignKey(Chategory,on_delete=models.SET_NULL,null=True)
    is_available = models.BooleanField(default=True)
    soled_count = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
   

    def save(self,*args,**kwargs):
        self.updated_date = timezone.now()
        if self.chategory:
            self.chategory.realatedproductscount()
        return super().save(*args,**kwargs)


class CartProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    
class Cart(models.Model):
    condition = (('ND',"NOTDELIVERED"),
                 ('D',"DELIVERED"),
                 ('O',"ONPROGRESS"),
                 ('C',"CANCLLED"))
    
    orderconditionchoices  = (('O','ORDERED'),
                       ('NO','NOT-ORDERED'))
    
    products = models.ManyToManyField(CartProduct,related_name='cart_products',blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    condition = models.CharField(max_length=2,choices=condition,default='ND')
    ordercondition = models.CharField(max_length=2,choices=orderconditionchoices,default='NO')
    date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)


    def save(self,*args,**kwargs):
        self.updated_date = timezone.now()
        
        return super().save(*args,**kwargs)

class BoostedProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    slogan = models.CharField(max_length=225,null=True)
    date = models.DateTimeField(default=timezone.now)