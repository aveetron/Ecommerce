from django.shortcuts import render,HttpResponseRedirect
from .forms import ProductForms
from django.contrib.auth.decorators import login_required

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
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print('problem')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print('prob')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))