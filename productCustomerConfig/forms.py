from django import forms
from .models import Product, Stock


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','details','catagory','buying_price','selling_price','image','status']



class StockForms(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'total_qty']