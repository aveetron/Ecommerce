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


# Create your views here.
def registration(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        passwordOne = request.POST.get("passwordOne")
        passwordTwo = request.POST.get("passwordTwo")
        lastLogin = datetime.now()
        dateJoined = datetime.now()
        if passwordOne == passwordTwo :
            User.objects.create_user(
                username=firstName + lastName,
                first_name=firstName,
                last_name=lastName,
                email=email,
                is_superuser=0,
                is_staff=0,
                password=passwordOne,
                last_login=lastLogin,
                date_joined=dateJoined,
                is_active=1,
            )
            return redirect("login")
        else:
            print('password didnot matched')
            message = 'User alrady exists'
            messages.warning(request, message)
            return render(request, 'registration.html')
    else:
        print("else block")
        return render(request, "registration.html")


def loginPage(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("login")


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
    
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return redirect("login")


@login_required(login_url='loginPage')
def userList(request):
    allAuthUser = AuthUser.objects.all()
    context = {
        'allAuthUser': allAuthUser
    }
    return render(request, 'adminUserList.html', context)