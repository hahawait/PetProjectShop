from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from product.models import Product


@login_required
def cart_detail(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    total_price = sum(item.total_price() for item in cart.items.all())
    return render(request, 'cart/detail.html', {'cart': cart, 'total_price': total_price})


@login_required
def add_to_cart(request, product_slug):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    product = get_object_or_404(Product, slug=product_slug)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
