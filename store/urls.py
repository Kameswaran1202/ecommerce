from django.contrib import admin
from django.urls import path,include
from store import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/checkout/',views.checkout,name='checkout'),
    path('login/',views.login,name='checkout'),

    path('update_item/',views.updateItem,name='update_item'),  
]
 