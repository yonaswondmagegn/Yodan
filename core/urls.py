from django.urls import path
from .views import CoreAuth,VerifayCoreAuthOtp


urlpatterns = [
    path('auth/',CoreAuth.as_view()),
    path('verify/',VerifayCoreAuthOtp.as_view())
]