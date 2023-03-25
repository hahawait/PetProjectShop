from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Cart(models.Model):
    """
    Модель корзины
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id}"
    
    def total_price(self):
        """Метод для вычисления общей стоимости товаров в корзине"""
        total = 0
        for item in self.items.all():
            total += item.total_price()
        return total


class CartItem(models.Model):
    """
    Модель элемента корзины
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price
