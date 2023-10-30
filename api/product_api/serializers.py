from rest_framework import serializers

from api.category_api.serializers import CategorySerializer
from store.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    # category = CategorySerializer(
    #     read_only=True, source='subcategory.category'
    # )
    category = serializers.ReadOnlyField(source='subcategory.category.name')

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'category',
            'subcategory',
            'price',
            'image',
        )
