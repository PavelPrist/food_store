from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from cart.models import Cart, CartItem


class CartItemForListSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    price = serializers.SerializerMethodField(read_only=True)
    total_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'price',
            'quantity',
            'total_price',
        )

    def get_price(self, obj):
        return obj.product.price

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price


class CartItemForCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = (
            'product',
            'quantity',
        )


class CartListSerializer(serializers.ModelSerializer):
    items = CartItemForListSerializer(many=True)
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    total_quantity = serializers.SerializerMethodField(read_only=True)
    total_cost = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_cost(self, obj):
        return sum(item.get_cost() for item in obj.items.all())


class CartCreateSerializer(
    WritableNestedModelSerializer,
    serializers.ModelSerializer,
):
    items = CartItemForCreateSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'items',
        )

    def to_representation(self, instance):
        return CartListSerializer(instance).data
