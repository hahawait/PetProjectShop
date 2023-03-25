from django.urls import path
from .views import cart_detail, add_to_cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<slug:product_slug>/', add_to_cart, name='cart_add'),
    path('remove/<int:cart_item_id>/', remove_from_cart, name='cart_remove'),
]
