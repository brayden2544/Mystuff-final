from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from catalog import models as cmod
from . import templater
from django.contrib.auth.decorators import user_passes_test
import datetime

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  '''Check for Authntication'''
  if request.user.is_authenticated():
    
    #Setup Datetime 
    date = datetime.datetime.now()
    day = date.day
    month = date.strftime('%B')
    year = date.year
    monthYear = (str(month) + ' ' + str(year))
    dayMonthYear = (str(day) + ' ' + str(month) + ' ' + str(year))
    
    #Query Database for the right Montly Account
    transactions = cmod.Comission.objects.filter(month = monthYear)

    
  

    template_vars = {
      'transactions': transactions,
      'monthYear': monthYear,

      
    }
    return templater.render_to_response(request, 'employee_transactions.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  


  
