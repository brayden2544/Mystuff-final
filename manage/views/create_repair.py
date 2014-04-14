from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test
import datetime

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
      '''Edits a single question'''
      
  
      form = CheckInRepairForm()
      date = datetime.datetime.now()
      
      if request.method == 'POST':
        form = CheckInRepairForm(request.POST)
        if form.is_valid():
          
          repair = mmod.Repair_Item()
          repair.customer = amod.User.objects.get(id=form.cleaned_data['customer_number'])
          repair.expected_return = date + datetime.timedelta(days=form.cleaned_data['number_of_days_to_repair']) 
          repair.repair_item = form.cleaned_data['repair_item']
          repair.issue = form.cleaned_data['issue']
          repair.status = mmod.Repair_Status.objects.get(status='Checked In')
          repair.repair_fees = form.cleaned_data['repair_fees']
          repair.date_in = date
          repair.save()
          return HttpResponseRedirect('/manage/repairs')
 
      tvars = {
        'form': form,
      }
      return templater.render_to_response(request, 'create_repair.html', tvars)
  else:
      return HttpResponseRedirect("/account/please_sign_in/")

    
  
# The variables that will be put on the form
class CheckInRepairForm(forms.Form):
  customer_number= forms.IntegerField()
  repair_item= forms.CharField()
  number_of_days_to_repair= forms.IntegerField()
  issue= forms.CharField()
  repair_fees = forms.DecimalField()


  

  
