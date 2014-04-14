from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test
import datetime
from datetime import datetime
from decimal import Decimal
import time

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
      
      rental = request.urlparams[0]
      rental_return = mmod.Rental.objects.get(id=request.urlparams[0]) 
  
      form = ReturnForm(initial={
        'pre_condition': rental_return.pre_condition,
      })
  
      if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
          rental_return.returned = True
          rental_return.post_condition = form.cleaned_data['post_condition']
          rental_return.damage_report = form.cleaned_data['damage_report']
          rental_return.damage_fees = form.cleaned_data['damage_fees']
          date_returned = datetime.now()
          dr_day = date_returned.day
          dr_month = date_returned.strftime('%m')
          dr_year = date_returned.year
          rental_return.date_returned = (str(dr_month) + '/' + str(dr_day) + '/' + str(dr_year))
          date_format = "%m/%d/%Y"
          expected_return_date = datetime.strptime(rental_return.expected_return, date_format)
          rental_return_date = datetime.strptime(rental_return.date_returned, date_format)
          total_days_late_string = str((rental_return_date-expected_return_date).days)
          total_days_late_integer = int(total_days_late_string)
          rental_return.total_days_late = total_days_late_integer
          
          print("<------------------------------------------------------>")
          print(total_days_late_integer)
          
          rental_return.save()
          return HttpResponseRedirect('/manage/rental_total_fees/' + str(rental))
 
      tvars = {
        'form': form,
      }
      
      return templater.render_to_response(request, 'rental_return.html', tvars)
 
  else:
    return HttpResponseRedirect("/account/please_sign_in/")


# Creates a new store and then redirects the user onto the Edit Store page using its new id
def process_request__new(request):
  new_brand = mmod.Brand()
  new_brand.save()
  return HttpResponseRedirect('/manage/edit_brand/' + str(new_brand.id) + '/')
  
# The variables that will be put on the form
class ReturnForm(forms.Form):
  pre_condition= forms.CharField()
  post_condition= forms.CharField()
  damage_report= forms.CharField()
  damage_fees= forms.DecimalField()
  


    


  
  
  