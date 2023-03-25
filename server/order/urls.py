from django.urls import path
from .views import order_list, order_create, order_detail

app_name = 'order'

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', order_create, name='order_create'),
    path('<int:order_id>/', order_detail, name='order_detail'),
]
