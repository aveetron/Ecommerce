from django.shortcuts import render,HttpResponseRedirect
from .forms import ProductForms
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