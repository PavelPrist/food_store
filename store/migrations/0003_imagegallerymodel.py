# Generated by Django 4.2.6 on 2023-11-01 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_product_id_slug_store_produ_id_2abda1_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='product_gallery/%Y/%m/', verbose_name='Будет приведено к ширине 300px')),
                ('product', models.ForeignKey(help_text='Фото товара', on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='store.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'изображение для галереи',
                'verbose_name_plural': 'изображения для галереи',
                'default_related_name': 'gallery',
            },
        ),
    ]
