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
from productCustomerConfig.models import Product,Stock, OrderDetail


# Create your views here.
def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        passwordOne = request.POST.get("passwordOne")
        passwordTwo = request.POST.get("passwordTwo")
        lastLogin = datetime.now()
        dateJoined = datetime.now()
        if passwordOne == passwordTwo :
            User.objects.create_user(
                username=username,
                email=email,
                is_superuser=0,
                is_staff=0,
                password=passwordOne,
                last_login=lastLogin,
                date_joined=dateJoined,
                is_active=1,
            )
            if username and passwordOne:
                user = authenticate(username=username, password=passwordOne)
                auth_login(request, user)
                user.save()
            return redirect("ecommerce")
        else:
            print('password didnot matched')
            message = 'password didnot matched'
            messages.warning(request, message)
            return render(request, 'shoppers/registration.html')
    else:
        print("else block")
        return render(request, "shoppers/registration.html")






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


from django.db.models import Sum


@login_required(login_url="loginPage")
def home(request):
    allProduct = Product.objects.all().order_by('-pk')
    totalStock = Stock.objects.all().order_by('-pk')
    totalProduct = Product.objects.count()
    orderDetails = OrderDetail.objects.all().order_by('-pk')
    totalOrder = OrderDetail.objects.all().count()
    orderPending = OrderDetail.objects.filter(delivered = False).count()
    totalRevenue = OrderDetail.objects.filter(delivered=True).aggregate(Sum('total'))['total__sum']
    context = {
        'allProduct': allProduct,
        'totalStock': totalStock,
        'totalProduct': totalProduct,
        'orderDetails': orderDetails,
        'totalOrder': totalOrder,
        'orderPending': orderPending,
        'totalRevenue': totalRevenue
    }   
    return render(request, "home.html", context)


def logout(request):
    auth.logout(request)
    return redirect("ecommerce")


def customerLoginPage(request):
    return render(request, 'shoppers/login.html')

def customerLoginCheck(request):
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
                return redirect("ecommerce")
            else:
                print("wrong username and password")
                return redirect("login")
        else:
            print("login failed")
            return redirect("login")
    else:
        print("login problem")
        return redirect("login")