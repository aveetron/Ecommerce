from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('addProduct', views.addProduct, name='addProduct'),
    path('addStock', views.addStock, name='addStock'),
    path('deleteProduct/<id>/',views.deleteProduct, name='deleteProduct'),
    path('deleteStock/<id>/',views.deleteStock, name='deleteStock'),
    path('deleteOrder/<id>/',views.deleteOrder, name='deleteOrder'),
    path('delivered/<id>/',views.delivered, name='delivered'),


]

