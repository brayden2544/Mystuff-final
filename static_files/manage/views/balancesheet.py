from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  '''Check for Authntication'''
  if request.user.is_authenticated():
    '''Shows all questions in the DB'''
    
    inventory = mmod.Inventory.objects.get(id=1)
    inventory_balance = 0
    available_products = mmod.Catalog_Item.objects.filter(availability = 1)
    for p in available_products:
      inventory_balance += (p.cost * p.product_count) 
    inventory.balance = inventory_balance
    
    
    cash = mmod.Cash.objects.get(id=1)
    PrepaidServiceLiability = mmod.PrepaidServiceLiability.objects.get(id=1)
    
  

    template_vars = {
      'inventory_balance': inventory_balance,
      'cash': cash,
      'PrepaidServiceLiability': PrepaidServiceLiability,
      
    }
    return templater.render_to_response(request, 'balancesheet.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
  
  

  
