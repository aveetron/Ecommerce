from django import forms
from .models import Product, Stock, Cart, OrderDetail

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','details','catagory','buying_price','selling_price','image','status']



class StockForms(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'total_qty']



class OrderDetailForms(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'