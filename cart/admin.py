from django.contrib import admin

from cart.models import Cart, CartItem
from store.models import Product


class CartItemProductInline(admin.StackedInline):
    model = CartItem
    raw_id_fields = ['product', ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'created_at',
        'updated_at',
        'get_total_price',
        'get_total_quantity',
    )
    list_filter = ('user', 'created_at', 'updated_at',)
    inlines = [CartItemProductInline]
