from djoser.serializers import UserCreateSerializer,UserSerializer as BaseUserSerializer

class UserRegisterSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id','username','phonenumber','password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','phonenumber']