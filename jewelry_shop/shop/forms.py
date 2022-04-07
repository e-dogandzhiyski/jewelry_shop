from jewelry_shop.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from jewelry_shop.shop.models import Product  # ProductPhoto
from django import forms


# class CreateProductForm(BootstrapFormMixin, forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('image', 'description', 'type', 'price', 'name')
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
        fields = ('name', 'type', 'price', 'image', 'description')
