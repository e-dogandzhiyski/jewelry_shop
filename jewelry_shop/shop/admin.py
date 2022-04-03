from django.contrib import admin
from jewelry_shop.shop.models import Product


class ProductInlineAdmin(admin.StackedInline):
    model = Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


