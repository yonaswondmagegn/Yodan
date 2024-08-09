from djoser.serializers import UserCreateSerializer,UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import User

class UserRegisterSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['phonenumber','password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','phonenumber']


class CoreAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phonenumber']