from rest_framework import serializers

from store.models import ImageGalleryModel, Product


class ImageGalleryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGalleryModel
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    category = serializers.ReadOnlyField(source='subcategory.category.name')
    gallery_images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'category',
            'subcategory',
            'price',
            'image',
            'gallery_images',
        )

    def get_gallery_images(self, obj):
        images = ImageGalleryModel.objects.filter(product=obj)
        return ImageGalleryModelSerializer(images, many=True).data
