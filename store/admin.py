from django.contrib import admin
from .models import Product,Chategory,Image,Cart,BoostedProduct,CartProduct


admin.site.register(Product)
admin.site.register(Chategory)
admin.site.register(Image)
admin.site.register(Cart)
admin.site.register(BoostedProduct)
admin.site.register(CartProduct)
# Register your models here.
