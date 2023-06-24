from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Cart(models.Model):
    """
    Модель корзины
    """

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

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

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price
