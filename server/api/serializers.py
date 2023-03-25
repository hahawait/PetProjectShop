from rest_framework import serializers
from product.models import Brand, Category, Product, ProductImage
from cart.models import Cart, CartItem
from order.models import Order, OrderItem

class BrandSerializer(serializers.ModelSerializer):
    """
    Сериализатор бренда
    """

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор категории товара
    """

    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор фотографии товара
    """

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор товара
    """

    brand = BrandSerializer()
    category = CategorySerializer()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'brand', 'category', 'images']

    def get_images(self, obj):
        images = obj.productimage_set.all()
        return ProductImageSerializer(images, many=True).data


class CartItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор элемента корзины
    """
    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity', 'total_price')


class CartSerializer(serializers.ModelSerializer):
    """
    Сериализатор корзины
    """
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created', 'updated', 'items', 'total_price')


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'cart', 'status', 'total_price', 'created_at', 'updated_at', 'order_items', 'total')

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        return [{"product_name": item.product.name, "quantity": item.quantity, "price": item.price} for item in order_items]

    def get_total(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        total = sum([item.price for item in order_items])
        return total
