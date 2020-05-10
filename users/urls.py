from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('loginCheck', views.loginCheck , name='loginCheck'),
    path('logout', views.logout, name='logout'),
]
