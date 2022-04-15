from django.contrib import admin

from jewelry_shop.shopping_cart.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('ref_code', 'is_ordered', 'date_ordered', 'owner_id')
