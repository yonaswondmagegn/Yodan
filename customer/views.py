from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import CustomerSerializer
from .models import Customer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    

# Create your views here.
