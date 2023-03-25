from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart
from product.models import Product

class Order(models.Model):
    """
    Модель заказа
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total(self):
        items = self.orderitem_set.all()
        return sum([item.price for item in items])


class OrderItem(models.Model):
    """
    Модель элемента заказа
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.order.id} - {self.product.name}'

    def get_total(self):
        return self.quantity * self.price
