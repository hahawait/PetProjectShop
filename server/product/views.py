from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    """
    Представление для списка товаров
    """

    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    """
    Представление для товара
    """

    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
