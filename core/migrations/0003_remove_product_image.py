# Generated by Django 5.0.4 on 2024-05-15 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
