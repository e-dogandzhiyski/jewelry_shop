# Generated by Django 3.2.12 on 2022-03-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Ring', 'Ring'), ('Necklace', 'Necklace'), ('Chain', 'Chain'), ('Earrings', 'Earrings')], default='no type', max_length=8),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('tagged_product', models.ManyToManyField(to='shop.Product')),
            ],
        ),
    ]