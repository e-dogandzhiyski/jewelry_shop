# Generated by Django 3.2.12 on 2022-04-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to=''),
        ),
    ]
