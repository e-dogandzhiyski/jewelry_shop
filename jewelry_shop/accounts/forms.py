from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from jewelry_shop.accounts.models import Profile, ShippingAddress, CardInfo
from jewelry_shop.common.helpers import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN,
    )
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
        }


class ShippingAddressForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # self._init_bootstrap_form_controls()

    def save(self, commit=True):
        shipping_address = super().save(commit=False)

        shipping_address.user = self.user
        if commit:
            shipping_address.save()

        return shipping_address

    class Meta:
        model = ShippingAddress
        fields = ('address', 'city', 'zip_code', 'phone_number')
        widgets = {
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Enter shipping address',
                }
            ),

            'zip_code': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Zip code',
                }
            ),

            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your phone number',
                }
            ),
        }


class CardInfoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # self._init_bootstrap_form_controls()

    def save(self, commit=True):
        shipping_address = super().save(commit=False)

        shipping_address.user = self.user
        if commit:
            shipping_address.save()

        return shipping_address

    class Meta:
        model = CardInfo
        fields = ('card_number', 'cvv', 'expiration_date')
        widgets = {
            'card_number': forms.TextInput(
                attrs={
                    'placeholder': 'Card Number',
                }
            ),

            'cvv': forms.TextInput(
                attrs={
                    'placeholder': 'CVV',
                }
            ),

            'expiration_date': forms.TextInput(
                attrs={
                    'placeholder': 'Valid to:',
                }
            ),
        }
