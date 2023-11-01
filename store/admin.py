from django.contrib import admin
from django.utils.html import format_html

from .models import Category, ImageGalleryModel, SubCategory, Product


class GalleryImageInline(admin.TabularInline):
    model = ImageGalleryModel
    readonly_fields = ('image_tmb',)
    fields = ('image', 'image_tmb')
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def form_html(self, obj, width, height):
        return format_html(
            f'<img src="{obj.image.url}" width="{width}" height="{height}" />'
        )

    def image_tag(self, obj):
        return self.form_html(obj, 150, 150)

    list_display = ('id', 'name', 'image', 'image_tag')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    list_editable = ('name', 'image')
    readonly_fields = ('image_tag',)
    image_tag.short_description = 'Изображение 150x150'


@admin.register(SubCategory)
class SubCategoryAdmin(CategoryAdmin):
    list_display = ('id', 'name', 'image', 'category', 'image_tag')
    list_editable = ('name', 'image', 'category')


@admin.register(Product)
class ProductAdmin(CategoryAdmin):
    def image_tag_middle(self, obj):
        return self.form_html(obj, 100, 100)

    def image_tag_small(self, obj):
        return self.form_html(obj, 50, 50)

    list_display = (
        'id',
        'name',
        'subcategory',
        'price',
        'description',
        'image_tag',
        'image_tag_middle',
        'image_tag_small',
        'image',
    )
    list_editable = ('image', 'subcategory', 'price', 'description')
    readonly_fields = ('image_tag', 'image_tag_middle', 'image_tag_small')
    image_tag_middle.short_description = 'Изображение 100x100'
    image_tag_small.short_description = 'Изображение 50x50'
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')
    inlines = [GalleryImageInline]


@admin.register(ImageGalleryModel)
class ImageGalleryModelAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'product')
