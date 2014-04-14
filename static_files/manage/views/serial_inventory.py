from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
    '''Shows all questions in the DB'''
    inventory = mmod.Serial_Inventory.objects.exclude(active=False).order_by('id')
                            
 
    #shoing the user auth system can delete later
    #print(">>>>>>>>"), request.user)
    #print("<<<<<<<<"), request.session)
  

    template_vars = {
      'inventory': inventory,
    }
    return templater.render_to_response(request, 'serial_inventory.html', template_vars)
  
  else:
      return HttpResponseRedirect("/account/please_sign_in/")

  
