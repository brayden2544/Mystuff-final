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
    
    rental = mmod.Rental.objects.get(id=request.urlparams[0])
    if rental.total_days_late > 0:
      rental.late_fees = rental.rental_item.daily_rent_rate * rental.total_days_late
    else:
      rental.late_fees = 0.0
    
    
    rental.save()
    

    template_vars = {
      'rental': rental,
    }
    return templater.render_to_response(request, 'rental_total_fees.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
  
  

  
