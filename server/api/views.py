from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from product.models import Product, Category, Brand
from cart.models import Cart
from order.models import Order
from .serializers import (BrandSerializer, CategorySerializer, ProductSerializer, CartSerializer, OrderSerializer)
from .permissions import AdminOrStafOrReadOnly


class ProductViewSet(ModelViewSet):
    """
    Представление для работы с товарами
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminOrStafOrReadOnly]
    search_fields = ['name', 'brand', 'category', 'price']


class CategoryViewSet(ModelViewSet):
    """
    Представление для работы с категориями
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrStafOrReadOnly]


class BrandViewSet(ModelViewSet):
    """
    Представление для работы с категориями
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AdminOrStafOrReadOnly]


class CartViewSet(ModelViewSet):
    """
    Представление для работы с корзиной
    """
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class OrderViewSet(ModelViewSet):
    """
    Представление для работы с заказом
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = self.request.user.cart
        order = serializer.save(user=self.request.user, cart=cart)
        cart.clear()







