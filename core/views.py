from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta
from rest_framework.views import APIView
from .models import User,AuthVerification
from rest_framework.response import Response
from rest_framework import status
from .coreserializer import CoreAuthUserSerializer
from .utils import generate_random_text,send_otp
from djoser.utils import login_user


#core auth get phonenumber

class CoreAuth(APIView):
   
    def post(self,request):
        phonenumber = request.data.get('phonenumber')
        if not phonenumber:
            return Response({'error':'phonenumber field is requred'},status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(phonenumber = phonenumber).first()
        if not user:
            user = User.objects.create(phonenumber = phonenumber)
        serializer = CoreAuthUserSerializer(user)
        try:
            otp_response  = send_otp(phonenumber)
            generated_unique_id = generate_random_text()
            print(generated_unique_id)
            serializer_copy = serializer.data.copy()
            serializer_copy['unique_id'] = generated_unique_id
            AuthVerification.objects.create(user = user,code = otp_response['code'],unique_id = generated_unique_id)
            return Response(serializer_copy,status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error':'cant send otp'},status=status.HTTP_400_BAD_REQUEST)


class VerifayCoreAuthOtp(APIView):
    def post(self,request):
        unique_id = request.data.get('unique_id')
        code = request.data.get('code')
        phonenumber = request.data.get('phonenumber')

        if not unique_id:
            return Response({'error':'unique_id not provided'},status=status.HTTP_400_BAD_REQUEST)
        if not code:
            return Response({'error':'code is requred field'},status=status.HTTP_400_BAD_REQUEST)
        if not phonenumber:
            return Response({'error':'phonenumber is requred field'},status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(phonenumber = phonenumber).first()
        if not user:
            return Response({'error':'user not found try again'},status=status.HTTP_404_NOT_FOUND)
        
        verify_auth = AuthVerification.objects.filter(user = user,unique_id = unique_id,code = code,).first()
        if not verify_auth:
            return Response({'error':'can/t verify wrong otp  try again '},status=status.HTTP_404_NOT_FOUND)
        
        if verify_auth.is_used:
            return Response({'error':"this code used before"},status=status.HTTP_400_BAD_REQUEST)
        expire_date_time = verify_auth.date +timedelta(minutes=1)
        current_date_time = timezone.now()


        if current_date_time  > expire_date_time:
            verify_auth.is_expired = True
            verify_auth.save()
            return Response({'error':'token expired try again '},status=status.HTTP_401_UNAUTHORIZED)

        user.is_active = True
        verify_auth.is_verified = True
        verify_auth.is_used = True
        
        user.save()
        verify_auth.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Print tokens for debugging (optional)
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")

        # Return tokens in response
        return Response({
            'access': access_token,
            'refresh': refresh_token,
        }, status=status.HTTP_200_OK)
        

        

