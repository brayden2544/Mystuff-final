from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test
import datetime

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  '''Check for Authntication'''
  if request.user.is_authenticated():
    
    #Setup Datetime 
    date = datetime.datetime.now()
    month = date.strftime('%B')
    year = date.year
    monthYear = (str(month) + ' ' + str(year))
    print(monthYear)
    
    #Query Database for the right Montly Account
    revenue = mmod.Revenue.objects.get(account_name = monthYear)
    ComissionsExpense = mmod.ComissionsExpense.objects.get(account_name = monthYear)
    SalesTaxPayable = mmod.SalesTaxPayable.objects.get(account_name = monthYear)
    
  

    template_vars = {
      'revenue': revenue,
      'ComissionsExpense': ComissionsExpense,
      'SalesTaxPayable': SalesTaxPayable,
      'month': month,
      'year': year,
      
    }
    return templater.render_to_response(request, 'incomesheet.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
  
  

  
