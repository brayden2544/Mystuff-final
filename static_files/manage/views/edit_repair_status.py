from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.core.mail import EmailMessage

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
      
      repair = mmod.Repair_Item.objects.get(id=request.urlparams[0])
      customer = repair.customer
  
      form = EditStatusForm()
    
      
      if request.method == 'POST':
        form = EditStatusForm(request.POST)
        if form.is_valid():
        
          repair.status = form.cleaned_data['status']
          try:
            if repair.status == mmod.Repair_Status.objects.get(status='Ready For Pickup'): 
              send_mail('Repair Complete', 'Here is the message.', 'austen@byuisys.com',
                ['austensmackbyu@gmail.com'], fail_silently=False)
          except Exception:
            print('Email Send Failed')
            
          
          repair.damage_report = form.cleaned_data['damage_report']
          repair.save()
                        
          return HttpResponseRedirect('/manage/repairs')
 
      tvars = {
        'form': form,
        'repair': repair,
        'customer': customer,
      }
      return templater.render_to_response(request, 'edit_repair_status.html', tvars)
  else:
      return HttpResponseRedirect("/account/please_sign_in/")

    
  
# The variables that will be put on the form
class EditStatusForm(forms.Form):
  status = forms.ModelChoiceField(queryset= mmod.Repair_Status.objects.all())
  damage_report= forms.CharField()


  

  
