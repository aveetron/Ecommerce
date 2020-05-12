from django.shortcuts import render,HttpResponseRedirect
from .forms import ProductForms, StockForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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