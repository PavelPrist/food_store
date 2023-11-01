from django.contrib import admin
from django.db import models

from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='покупатель',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'Корзина пользователя {self.user}'

    @admin.display(ordering='get_total_price', description='Общая стоимость')
    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())

    @admin.display(
        ordering='get_total_quantity', description='Общее количество')
    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    @admin.display(ordering='get_product_price', description='Цена')
    def get_product_price(self):
        return self.item.get_price()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='корзина',
    )
    product = models.ForeignKey(
        'store.Product',
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='продукт',
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='количество',
    )

    def get_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.name}, Цена: {self.product.price}'

    class Meta:
        ordering = ('id',)
        verbose_name = 'товар в корзине'
        verbose_name_plural = 'товары в корзине'
