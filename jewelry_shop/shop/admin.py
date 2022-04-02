from django.contrib import admin

from jewelry_shop.shop.models import Product # ProductPhoto


class ProductInlineAdmin(admin.StackedInline):
    model = Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


# @admin.register(ProductPhoto)
# class ProductPhotoAdmin(admin.ModelAdmin):
#     pass
