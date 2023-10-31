from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
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
