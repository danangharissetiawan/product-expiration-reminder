from django.contrib.auth.models import User
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


class ProductNonPackagingForm(forms.ModelForm):
    class Meta:
        model = ProductNonPackaging
        fields = ['name', 'description', 'category', 'quality']
        exclude = ['user', 'slug', 'date_added', 'label', 'expiry_date']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        exclude = ['user', 'slug', 'date_added']

