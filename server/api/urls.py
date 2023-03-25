from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProductViewSet, CategoryViewSet, BrandViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'cart', CartViewSet, basename='cart') # basename т.к. во вьюхе нет queryset
router.register(r'order', OrderViewSet) # basename т.к. во вьюхе нет queryset

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
