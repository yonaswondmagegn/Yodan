from rest_framework import serializers
from .models import Customer
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','phonenumber',"is_staff"]

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = "__all__"