from django.db import models


class SlugBaseModel(models.Model):
    slug = models.SlugField(
        'Постоянная ссылка',
        max_length=255,
        unique=True,
        db_index=True,
        help_text='Введите постоянную ссылку'
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    class Meta:
        abstract = True


class Category(SlugBaseModel):
    name = models.CharField(
        'Наименование категории',
        max_length=255,
        unique=True,
        db_index=True,
        help_text='Введите наименование категории'
    )
    image = models.ImageField(
        'Изображение категории',
        upload_to='image/category_img/%Y/%m/%d/',
        help_text='Загрузите изображение категории'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class SubCategory(SlugBaseModel):
    name = models.CharField(
        'Наименование подкатегории',
        max_length=255,
        unique=True,
        db_index=True,
        help_text='Введите наименование подкатегории'
    )
    image = models.ImageField(
        'Изображение подкатегории',
        upload_to='subcategory_img/%Y/%m/%d/',
        help_text='Загрузите изображение подкатегории'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='категория',
        help_text='Выберите категорию'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class Product(SlugBaseModel):
    name = models.CharField(
        'Наименование продукта',
        max_length=255,
        unique=True,
        db_index=True,
        help_text='Введите наименование продукта'
    )
    image = models.ImageField(
        'Изображение продукта',
        upload_to='product_img/%Y/%m/%d/',
        help_text='Загрузите изображение продукта'
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='подкатегория',
        help_text='Выберите подкатегорию'
    )
    price = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=0,
    )
    description = models.TextField(
        'Описание',
        help_text='Введите описание продукта',
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        index_together = [
            ['id', 'slug'],
        ]
