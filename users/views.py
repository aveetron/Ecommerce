from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .models import * 
import datetime
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import auth
from django.contrib import messages
from django.db.models import Sum
from productCustomerConfig.models import Product,Stock


# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def loginCheck(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                user.save()
                print("logged in successfully")
                message = "you are successfully logged in"
                messages.success(request, message)
                return redirect("home")
            else:
                print("wrong username and password")
                return redirect("login")
        else:
            print("login failed")
            return redirect("login")
    else:
        print("login problem")
        return redirect("login")


@login_required(login_url="loginPage")
def home(request):
    allProduct = Product.objects.all().order_by('-pk')
    totalStock = Stock.objects.all().order_by('-pk')
    totalProduct = Product.objects.count()
    context = {
        'allProduct': allProduct,
        'totalStock': totalStock,
        'totalProduct': totalProduct
    }   
    return render(request, "home.html", context)


def logout(request):
    auth.logout(request)
    return redirect("login")


