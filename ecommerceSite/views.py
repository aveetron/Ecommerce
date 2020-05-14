from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from productCustomerConfig.models import Product,Cart,OrderDetail
from django.contrib import messages
from django.contrib.auth.models import User
from productCustomerConfig.forms import OrderDetailForms

# Create your views here.
def ecommerce(request):
    allProduct = Product.objects.filter(status = True)
    totalCart = Cart.objects.filter(customer = request.user.id).count()
    context = {
        'allProduct': allProduct,
        'totalCart': totalCart
    }
    return render(request, 'shoppers/index.html', context)





def addToCart(request, id):
    cart = Cart(
        product = Product.objects.get(id =id),
        customer = User.objects.get(id = request.user.id),
        status = True
    )
    cart.save()
    message = 'Product added to cart'
    messages.success(request, message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cartPage(request):
    totalCart = Cart.objects.filter(customer = request.user.id).count()
    allCart = Cart.objects.filter(customer = request.user.id)
    context = {
        'totalCart': totalCart,
        'allCart': allCart
    }
    return render(request, 'shoppers/cart.html', context)

def OrderDetailSave(request, id):
    cart = Cart.objects.get(id = id)
    if request.method == "POST":
        request.POST = request.POST.copy()
        form = OrderDetailForms(request.POST)
        if form.is_valid():
            orderInstance = form.save(commit=False)
            orderInstance.product = Product.objects.get(id = cart.product.id)
            orderInstance.customer = User.objects.get(id = request.user.id)
            orderInstance.total = 
            orderInstance.status = True
            orderInstance.save()
            message = 'Order Saved'
            messages.success(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'Order problem'
            messages.info(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        message = 'Order problem'
        messages.info(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))