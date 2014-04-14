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
    

    template_vars = {
      'month': month,
      'year': year,
      
    }
    return templater.render_to_response(request, 'new_month.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
def process_request__create(request):
  '''Check for Authntication'''
  if request.user.is_authenticated():
    
    # Setup new Month
    date = datetime.datetime.now()
    month = date.strftime('%B')
    year = date.year
    monthYear = (str(month) + ' ' + str(year))
    
    template_vars = {
      'month': month,
      'year': year,
    }
    
    try:
      #Query Database for the right Montly Account
      revenue = mmod.Revenue.objects.get(account_name = monthYear)
      
      return templater.render_to_response(request, 'new_month_fail.html', template_vars)

       
    except:
      # Setup Income Statement Accounts 
      newRevenueAccount = mmod.Revenue()
      newRevenueAccount.account_name = (str(month) + ' ' + str(year))
      newRevenueAccount.balance = 0
      newRevenueAccount.save()
    
      newComissionsExpenseAccount = mmod.ComissionsExpense()
      newComissionsExpenseAccount.account_name = (str(month) + ' ' + str(year))
      newComissionsExpenseAccount.balance = 0
      newComissionsExpenseAccount.save()
    
      newSalesTaxPayableAccount = mmod.SalesTaxPayable()
      newSalesTaxPayableAccount.account_name = (str(month) + ' ' + str(year))
      newSalesTaxPayableAccount.balance = 0
      newSalesTaxPayableAccount.save()
      

    
    return templater.render_to_response(request, 'new_month_complete.html', template_vars)
   
  else:
      return HttpResponseRedirect("/account/please_sign_in/") 

  
