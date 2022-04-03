from django.contrib import admin

from jewelry_shop.accounts.models import Profile, AppUser


# from jewelry_shop.shop.admin import ProductInlineAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (ProductInlineAdmin,)
    list_display = ('first_name', 'last_name')


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email',)
