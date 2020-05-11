from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','details','catagory','buying_price','selling_price','image','status']