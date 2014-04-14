from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from decimal import Decimal

def process_request(request):
   '''Finds all items for a certain category'''
   
   cart = request.session.get('cart', {})
   rental_cart = request.session.get('rental_cart', {})
   repair_cart = request.session.get('repair_cart', {})
   
   cart_items = []
   rental_items = []
   repair_items = []
   
   subtotal = 0
   
   comission = 0
   
   for i in cart:
       product_info = []
       product_object = mmod.Catalog_Item.objects.get(id=i)
       product_info.append(product_object)
       quantity = cart[i]
       subtotal += product_object.price * quantity
       comission_subtotal = product_object.price * product_object.comission_rate
       product_info.append(quantity)
       cart_items.append(product_info)
    
   for r in rental_cart:
       product_info = []
       product_object = mmod.Catalog_Item.objects.get(id=r)
       product_info.append(product_object)
       rental_option = Decimal(rental_cart[r])
       subtotal += product_object.daily_rent_rate * Decimal(rental_option)
       product_info.append(rental_option)
       rental_items.append(product_info)
    
   for a in repair_cart:
       repair_info = []
       repair_object = mmod.Repair_Item.objects.get(id=a)
       repair_info.append(repair_object)
       subtotal += repair_object.repair_fees
       repair_items.append(repair_info)
   
   tvars = {
       'cart_items': cart_items,
       'rental_items': rental_items,
       'repair_items': repair_items,
       'subtotal': subtotal,
   }

   return templater.render_to_response(request, 'cart.html', tvars)
   
def process_request__delete(request):
    i = request.urlparams[0]
    cart = request.session.get('cart', {})
    del cart[i]
    request.session['cart'] = cart
    return HttpResponseRedirect('/catalog/cart')
    
def process_request__rental_delete(request):
    i = request.urlparams[0]
    rental_cart = request.session.get('rental_cart', {})
    del rental_cart[i]
    request.session['rental_cart'] = rental_cart
    return HttpResponseRedirect('/catalog/cart')

def process_request__repair_delete(request):
    i = request.urlparams[0]
    repair_cart = request.session.get('repair_cart', {})
    del rental_cart[i]
    request.session['repair_cart'] = repair_cart
    return HttpResponseRedirect('/catalog/cart')