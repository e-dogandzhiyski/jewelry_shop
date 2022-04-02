from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from jewelry_shop.accounts.managers import AppUserManager
from jewelry_shop.common.validators import validate_only_letters


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    email = models.EmailField()

    USERNAME_FIELD = 'username'

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

    # username = models.CharField(
    #     max_length=20,
    #     unique=True,
    #     null=False,
    #     blank=False,
    # )

    email = models.EmailField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
