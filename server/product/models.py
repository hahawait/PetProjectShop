from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Brand(models.Model):
    """
    Модель бренда
    """

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('brand_detail', args=[str(self.slug)])


class Category(models.Model):
    """
    Модель категории товара
    """

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])


class Product(models.Model):
    """
    Модель товара
    """

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('product-detail', kwargs={'pk': self.pk})
        return reverse('product_detail', args=[str(self.slug)])


class ProductImage(models.Model):
    """
    Модель фотографии товара
    """

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')

    def __str__(self):
        return self.product.name + ' Image'
