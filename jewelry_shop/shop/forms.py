from jewelry_shop.common.helpers import BootstrapFormMixin
from jewelry_shop.shop.models import Product  # Product
from django import forms


# class CreateProductForm(BootstrapFormMixin, forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#
#     RING = "Ring"
#     NECKLACE = "Necklace"
#     CHAIN = "Chain"
#     EARRINGS = "Earrings"
#     PRODUCT_NAME_MAX_LEN = 30
#     TYPES = [(x, x) for x in (RING, NECKLACE, CHAIN, EARRINGS)]
#
#     name = forms.CharField(
#         max_length=PRODUCT_NAME_MAX_LEN,
#         # null=False,
#         # blank=False,
#     )
#
#     type = forms.ChoiceField(
#         # max_length=max(len(x) for (x, _) in TYPES),
#         choices=TYPES,
#     )
#
#     description = forms.CharField(
#         widget={
#             forms.Textarea
#         }
#     )
#
#     image = forms.ImageField(
#         # upload_to=IMAGE_UPLOAD_TO_DIR,
#         null=True,
#         blank=True,
#         # default='no_image.png'
#     )
#
#     price = forms.FloatField(
#         null=False,
#         blank=False,
#     )
#
#     def save(self, commit=True):
#         product = Product(
#             name=self.cleaned_data['name'],
#             type=self.cleaned_data['type'],
#             description=self.cleaned_data['description'],
#             image=self.cleaned_data['image'],
#             price=self.cleaned_data['price'],
#         )
#
#         if commit:
#             return product.save()
#         return product
#
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
