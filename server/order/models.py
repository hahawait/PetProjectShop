from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart
from product.models import Product


class Order(models.Model):
    """
    Модель заказа
    """

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    status = models.CharField(max_length=20, verbose_name='Статус')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'Order {self.id}'

    def get_total(self):
        items = self.orderitem_set.all()
        return sum([item.price for item in items])


class OrderItem(models.Model):
    """
    Модель элемента заказа
    """

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'Order {self.order.id} - {self.product.name}'

    def get_total(self):
        return self.quantity * self.price
