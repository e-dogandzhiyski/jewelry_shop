# Generated by Django 3.2.12 on 2022-04-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220329_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='image',
            field=models.ImageField(default='no_image.png', upload_to='mediafiles'),
        ),
    ]
