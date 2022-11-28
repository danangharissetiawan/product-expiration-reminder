from django.utils.text import slugify
from django import forms

from .models import ProductPackaging, ProductNonPackaging, Barcode
from .utils.management import label_expiry_date


class ProductPackagingForm(forms.ModelForm):
    barcode_input = forms.CharField(max_length=43, required=True)

    class Meta:
        model = ProductPackaging
        fields = ['name', 'description', 'expiry_date', 'category', 'barcode_input']
        exclude = ['user', 'slug', 'date_added', 'label', 'barcode']




    # def clean_barcode(self):
    #     barcode = "8998989110129"
    #     if not Barcode.objects.filter(barcode=barcode).exists():
    #         raise forms.ValidationError("Barcode tidak terdaftar")
    #     else:
    #         barcode = Barcode.objects.get(barcode=barcode).first()
    #         return barcode
    #
    # def save(self, **kwargs):
    #     slug_str = f"{kwargs['name']}-{kwargs['expiry_date']}"
    #     print(self.barcode)
    #     self.barcode = self.clean_barcode()
    #     self.label = label_expiry_date(kwargs['expiry_date'])
    #     self.slug = slugify(slug_str)
    #
    #     super().save(**kwargs)

