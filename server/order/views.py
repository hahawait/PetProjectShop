from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from cart.models import Cart
from .models import Order, OrderItem
from .tasks import send_order_confirmation_email


@login_required
def order_create(request):
    cart = Cart.objects.get(user=request.user)

    if request.method == 'POST':
        # Извлекаем из формы необходимые данные
        status = 'created'
        total_price = request.POST.get('total_price')
        order = Order.objects.create(user=request.user, cart=cart, status=status, total_price=total_price)

        # Отправляем письмо на почту пользователя
        send_order_confirmation_email.delay(order.id)

        # Получаем список элементов корзины и сохраняем их в элементах заказа
        cart_items = cart.items.all()
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.total_price())

        return redirect(reverse('order:order_detail', args=[order.id]))
    else:
        # Отображаем форму для оформления заказа с указанием общей стоимости
        total_price = cart.total_price()
        return render(request, 'order/order_detail.html', {'total_price': total_price})


@login_required
def order_list(request):
    """
    Представление для списка заказов пользователя
    """
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders
    }
    return render(request, 'order/order_list.html', context)


@login_required
def order_detail(request, order_id):
    """
    Представление для деталей заказа
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order
    }
    return render(request, 'order/order_detail.html', context)
