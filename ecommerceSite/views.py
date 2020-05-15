from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
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
    if Cart.objects.filter(product = Product.objects.get(id =id), customer= request.user.id).exists():
        message = 'already added to cart'
        messages.info(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
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


def cartDetailSave(request, id):
    cart = Cart.objects.get(id = id)
    cart.qty = request.POST.get('qty')
    print(cart.qty)
    if cart.qty == 1:
        cart.total = float(cart.product.selling_price) * 1
    else:
        cart.total = float(cart.product.selling_price) * float(cart.qty)
    cart.status = True
    cart.save()
    message = 'Product added on Order list'
    messages.success(request, message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def deleteCart(request, id):
    cart = Cart.objects.get(id =id)
    cart.delete()
    message = 'Product deleted successfully'
    messages.success(request, message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def checkOutPage(request):
    allCart = Cart.objects.filter(customer = request.user.id)
    total = 0
    for cart in Cart.objects.filter(customer = request.user.id):
        total += (cart.qty * cart.product.selling_price)

    shippingCost = 20
    total = total + shippingCost
    context = {
        'allCart': allCart,
        'total': total
    }
    return render(request, 'shoppers/checkout.html', context)




def orderSubmit(request):
    if request.method == 'POST':
        total = 0
        productDetails = ''
        for cart in Cart.objects.filter(customer = request.user.id):
            total += (cart.qty * cart.product.selling_price)
            productDetails = productDetails + str(cart.product.name) + str(cart.qty)
        
        product = productDetails
        customer = User.objects.get(id = request.user.id)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        total  = total + 20
        status = True
        order = OrderDetail(
            product = product,
            customer = customer,
            address = address,
            phone = phone,
            total = total,
            status = status,
        )
        order.save()
        message =  'order submitted'
        messages.success(request, message)
        return redirect('ecommerce')
    else:
        message =  'order submit problem'
        messages.success(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

