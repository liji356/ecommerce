# Generated by Django 3.2.7 on 2023-09-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_rename_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]