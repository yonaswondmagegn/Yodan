from rest_framework import serializers
from .models import Chategory,Image,Product,Cart,BoostedProduct,CartProduct
from customer.serializer import CustomerSerializer


class ChategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Chategory
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many = True)
    class Meta:
        model = Product 
        fields = '__all__'

class ProductSerializerForCart(serializers.ModelSerializer):
    images = ImageSerializer(many = True)
    # images = ImageSerializer(many = True)
    class Meta:
        model = Product 
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializerForCart()
    class Meta:
        model = CartProduct
        fields = '__all__'

class CartProductFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields  ='__all__'

class ProductSerializerWithImage(serializers.ModelSerializer):
    images = ImageSerializer(many = True)
    class Meta:
        model = Product 
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer()
    class Meta:
        model = Cart
        fields = "__all__"

class BoostSerializer(serializers.ModelSerializer):
    product = ProductSerializerWithImage()
    class Meta:
        model = BoostedProduct
        fields = "__all__"