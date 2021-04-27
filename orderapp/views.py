from django.shortcuts import render,redirect
from .models import Cart,Product,User

def addtocart(request,id):
    uid=request.session.get('uid')
    c=Cart()
    product=Product.objects.get(id=id)
    user=User.objects.get(id=uid)
    c.product=product
    c.user=user
    c.save()
    return redirect('/')