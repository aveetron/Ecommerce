from django.shortcuts import render,HttpResponseRedirect
from .forms import ProductForms, StockForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here.
@login_required(login_url="loginPage")
def addProduct(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        # request.POST.status = 1
        form = ProductForms(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            productInstance = form.save(commit=False)
            productInstance.status = True
            productInstance.save()
            form.save()
            message = 'item created successfully'
            messages.success(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'Problem Item creation'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        message = 'Problem Item creation'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='loginPage')
def addStock(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        form = StockForms(request.POST)
        print(request.POST)
        if form.is_valid():
            stockInstance = form.save(commit=False)
            stockInstance.status = True
            stockInstance.remain_qty = request.POST['total_qty']
            stockInstance.created_by = request.user.username
            stockInstance.save()
            message = 'Stock created successfully'
            messages.success(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'Problem Stock creation'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        message = 'Problem Stock creation'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='loginPage')
def deleteProduct(request, id):
    product = Product.objects.get(id = id)
    product.status = False
    product.save()
    message = 'product deleted'
    messages.info(request, message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='loginPage')
def deleteStock(request, id):
    stock = Stock.objects.get(id = id)
    stock.status = False
    stock.save()
    message = 'stock deleted'
    messages.info(request, message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='loginPage')
def deleteOrder(request, id):
    order = OrderDetail.objects.get(id = id)
    order.status = False
    order.save()
    message = 'order deleted'
    messages.info(request, message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='loginPage')
def delivered(request, id):
    order = OrderDetail.objects.get(id = id)
    order.delivered = True
    order.save()
    message = 'order Delivered'
    messages.info(request, message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
