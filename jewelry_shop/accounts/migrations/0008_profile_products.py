# Generated by Django 3.2.12 on 2022-04-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_image'),
        ('accounts', '0007_auto_20220410_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(blank=True, to='shop.Product'),
        ),
    ]
