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
    
    inventory= mmod.Inventory.objects.all()
    inventory.delete()
    
    cash = mmod.Cash.objects.all()
    cash.delete()
    
    PrepaidServiceLiability = mmod.PrepaidServiceLiability.objects.all()
    PrepaidServiceLiability.delete()
    
    revenue = mmod.Revenue.objects.all()
    revenue.delete()
    
    ComissionsExpense = mmod.ComissionsExpense.objects.all()
    ComissionsExpense.delete()
    
    SalesTaxPayable = mmod.SalesTaxPayable.objects.all()
    SalesTaxPayable.delete()
    
    store= mmod.Store.objects.all()
    store.delete()
    
    category = mmod.Category.objects.all()
    category.delete()
  
    brand = mmod.Brand.objects.all()
    brand.delete()
    
    serial_products = mmod.Serial_Inventory.objects.all()
    serial_products.delete()
    
    
    bulk_products = mmod.Bulk_Inventory.objects.all()
    bulk_products.delete()
    
    rentals = mmod.Rental.objects.all()
    rentals.delete()
    
    repairs = mmod.Repair_Item.objects.all()
    repairs.delete()

    template_vars = {

    }
    return templater.render_to_response(request, 'Remove_All.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
  
  

  
