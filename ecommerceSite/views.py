from django.shortcuts import render

# Create your views here.
def ecommerce(request):
    return render(request, 'shoppers/index.html')