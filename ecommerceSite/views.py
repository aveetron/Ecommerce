from django.shortcuts import render
from productCustomerConfig.models import Product


# Create your views here.
def ecommerce(request):
    allProduct = Product.objects.filter(status = True)
    context = {
        'allProduct': allProduct
    }
    return render(request, 'shoppers/index.html', context)