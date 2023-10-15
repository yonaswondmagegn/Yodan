from django.urls import path
from .views import CustomerViewSet
from rest_framework_nested import routers

route = routers.DefaultRouter()

route.register('customer',CustomerViewSet)


urlpatterns = route.urls