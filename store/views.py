from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *


# Create your views here.
def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
    context={'items':items, 'order':order}
    return render(request,'cart.html',context)
def checkout(request): 
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
    context={'items':items, 'order':order}
    return render(request,'checkout.html',context)
def login(request):
    context={}
    return render(request,'login.html',context)

def updateItem(request):
    data= json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('Action:',action)
    print('Product:',productId)


    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created =Order.objects.get_or_create(customer=customer,complete=False) 

    orderItem, created = OrderItem.objects.get_or_create(customer=customer,complete=False)

    if action =='add':
        orderItem.quatity=(orderItem.quatity+1)
    elif action =='remove':
        orderItem.quatity=(orderItem.quatity-1)

    orderItem.save()

    if order.quantity <=0:
        orderItem.delete()
     
    return JsonResponse('Item was added', safe=False)
