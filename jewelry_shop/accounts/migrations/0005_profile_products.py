# Generated by Django 3.2.12 on 2022-04-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220401_1416'),
        ('accounts', '0004_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(blank=True, to='shop.Product'),
        ),
    ]