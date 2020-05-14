
from django.urls import path
from . import views
from users.views import registration,customerLoginCheck,customerLoginPage

urlpatterns = [
    path('', views.ecommerce, name='ecommerce'),
    path('addToCart/<id>/', views.addToCart, name='addToCart'),
    path('registration/', registration, name='registration'),
    path('customerLoginCheck', customerLoginCheck, name='customerLoginCheck'),
    path('customerLoginPage', customerLoginPage, name='customerLoginPage'),
    path('cartPage', views.cartPage, name='cartPage'),
    path('OrderDetailSave/<id>/', views.OrderDetailSave, name='OrderDetailSave'),
]

