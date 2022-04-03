from jewelry_shop.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from jewelry_shop.shop.models import Product  # ProductPhoto
from django import forms


class CreateProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'type', 'price', 'photo', 'description')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter product name',
                }
            ),
        }


# class DeleteProductForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#         self._init_disabled_fields()
#
#     def save(self, commit=True):
#         self.instance.delete()
#         return self.instance
#
#     class Meta:
#         model = Product
#         # exclude = ('tagged_product',)
#         fields = ('name', 'type', 'price', 'photo', 'description')
#         widgets = {
#             'name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Enter product name',
#                 }
#             ),
#         }


class DeleteProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Product
        fields = ('name', 'type', 'price', 'photo', 'description')

