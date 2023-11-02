from django.urls import path
from rest_framework_nested import routers
from .views import (
    ProductViewSet,
    ChategoryViewSet,
    CartViewSet,
    ImageViewSet,
    ImageNestedViewSet,
    BoostViewSet,
    CartProductViewSet,
    CartProductFullViewSet,
    BoostPostViewSet
    )

route = routers.DefaultRouter()
route.register('product',ProductViewSet)
route.register('chategory',ChategoryViewSet)
route.register('cart',CartViewSet)
route.register('image',ImageViewSet)
route.register('boost',BoostViewSet)
route.register('boostpost',BoostPostViewSet)
route.register('cartproducts',CartProductFullViewSet)
 
nested_route = routers.NestedDefaultRouter(route,'product',lookup = 'product')
nested_route.register('images',ImageNestedViewSet,basename='product-images')

cart_nested_route = routers.NestedDefaultRouter(route,'cart',lookup ='cart' )
cart_nested_route.register('cartproducts',CartProductViewSet,basename='cart-product')


urlpatterns = route.urls + nested_route.urls + cart_nested_route.urls
