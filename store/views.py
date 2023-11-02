from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import Chategory,Cart,Product,Image,BoostedProduct,CartProduct
from .pagination import ProductPagination,ChategoryPaginator
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .custompermition import isAdminOrReadOnly,creatorOrAdminOnly
User = get_user_model()

from .serializer import (
    ProductSerializer,
    ChategorySerializer,
    CartSerializer,
    ImageSerializer,
    CartProductSerializer,
    BoostSerializer,
    CartProductFullSerializer,
    BoostPostSerializer
)
from .filter import ChategoryFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
        ]
    filterset_fields = ['id','chategory']
    search_fields = ['title','description']
    pagination_class = ProductPagination
    serializer_class = ProductSerializer
    permission_classes = [isAdminOrReadOnly]
    
    def get_queryset(self):
        # if not User.objects.filter(is_superuser=True).exists():
        if not User.objects.get(username = 'yonasadmin'):
            user = User.objects.create(username ='yonasadmin',email= 'yonas@alksdj.com',phonenumber = 96331122,is_staff = True)
            user.set_password('YONASyonas@1996')
            user.save()
        # # if not User.objects.filter(is_superuser=True).exists():
        # #     user = User.objects.create(
        # #         username = 'yonas',
        # #         is_superuser = True,
        # #         email = "yonas@1996",
        # #         is_staff = True
        # #     )
        # #     user.set_password('yonas@1996')
        # #     user.save()
        return Product.objects.all()


class ChategoryViewSet(ModelViewSet):
    queryset = Chategory.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    order_fields = ['likedrating']
    pagination_class = ChategoryPaginator
    serializer_class = ChategorySerializer
    filterset_class = ChategoryFilter
    permission_classes = [isAdminOrReadOnly]

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [isAdminOrReadOnly]

class ImageNestedViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [isAdminOrReadOnly]

    def get_queryset(self):
        product_id = self.kwargs.get('product_pk')

        try:
            product = Product.objects.get(id = product_id)
        except:
            return Image.objects.none()
        
        return product.images

class CartProductViewSet(ModelViewSet):
    serializer_class = CartProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs.get('cart_pk')
        try:
            cart = Cart.objects.get(id = id)
        except:
            return CartProduct.objects.none()
        

        return cart.products

class CartProductFullViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductFullSerializer
    # permission_classes = [IsAuthenticated]

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['condition','customer','ordercondition']
    order_fields = ['id','date']
    serializer_class = CartSerializer
    # permission_classes = [IsAuthenticated]


class BoostViewSet(ModelViewSet):
    queryset = BoostedProduct.objects.all()
    serializer_class = BoostSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['active']
    order_fields = ['date']
    permission_classes = [isAdminOrReadOnly]

class BoostPostViewSet(ModelViewSet):
    queryset = BoostedProduct.objects.all()
    serializer_class = BoostPostSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['active']
    order_fields = ['date']
    permission_classes = [isAdminOrReadOnly]



    