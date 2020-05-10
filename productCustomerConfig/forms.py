from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        fields = '__all__'