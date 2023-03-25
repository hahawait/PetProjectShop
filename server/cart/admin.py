from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated')
    search_fields = ['user', 'created', 'updated']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ['cart', 'product', 'quantity']
    list_filter = ('cart', 'product')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
