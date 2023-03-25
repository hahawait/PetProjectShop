from django.contrib import admin
from .models import Brand, Category, Product, ProductImage


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'brand__name', 'category__name', 'price']
    list_filter = ('name', 'price')


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ['product__name']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
