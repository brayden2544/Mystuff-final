from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test

def process_request(request):
  '''Check for Authntication'''
  if request.user.is_authenticated():
    '''Shows all questions in the DB'''
    user = request.user
    repairs = mmod.Repair_Item.objects.filter(customer=user)
  

    template_vars = {
      'repairs': repairs,
    }
    return templater.render_to_response(request, 'view_repairs.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
def process_request__add_to_cart(request):
    repair = mmod.Repair_Item.objects.get(id=request.urlparams[0])
    
    if 'repair_cart' not in request.session:
        request.session['repair_cart'] = {}
        print("repair cart created")
        
    repair_cart = request.session.get('repair_cart', {})
    repair_id = str(repair.id)
    if repair_id in repair_cart:
        repair_cart[repair_id] = 1
    else:
        repair_cart[repair_id] = 1
    print("added to cart")
    request.session['repair_cart'] = repair_cart
    return HttpResponseRedirect('/catalog/cart/')
  
  
  

  
