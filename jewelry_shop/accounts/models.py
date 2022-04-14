from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from jewelry_shop.accounts.managers import AppUserManager
from jewelry_shop.common.validators import validate_only_letters, validate_only_numbers
from jewelry_shop.shop.models import Product


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 30

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    email = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.address}'


class ShippingAddress(models.Model):
    ADDRESS_MAX_LEN = 120
    PHONE_NUMBER_MAX_LEN = 10
    ZIP_CODE_MAX_LEN = 4
    SOFIA = "Sofia"
    PLOVDIV = "Plovdiv"
    VARNA = "Varna"
    BURGAS = "Burgas"
    RUSE = "Ruse"
    STARA_ZAGORA = "Stara Zagora"
    PLEVEN = "Pleven"
    SLIVEN = "Sliven"
    DOBRICH = "Dobrich"
    SHUMEN = "Shumen"

    CITIES = [(x, x) for x in (SOFIA, PLOVDIV, VARNA, BURGAS, PLEVEN, SLIVEN, DOBRICH, SHUMEN)]

    address = models.CharField(
        max_length=ADDRESS_MAX_LEN,
    )

    city = models.CharField(
        max_length=max(len(x) for (x, _) in CITIES),
        choices=CITIES
    )

    zip_code = models.CharField(
        max_length=ZIP_CODE_MAX_LEN,
        validators=(
            validate_only_numbers,
        )
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LEN,
        validators=(
            validate_only_numbers,
        )
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.city}, {self.address}'


class CardInfo(models.Model):
    CARD_MAX_LEN = 16
    CVV_MAX_LEN = 3

    card_number = models.CharField(
        max_length=CARD_MAX_LEN,
        validators={
            validate_only_numbers,
        }
    )

    cvv = models.CharField(
        max_length=CVV_MAX_LEN,
        validators={
            validate_only_numbers,
        }
    )

    expiration_date = models.DateTimeField(

    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
