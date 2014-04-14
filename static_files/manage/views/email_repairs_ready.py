from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail


@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
    
    repairs = mmod.Repair_Item.objects.filter(status = mmod.Repair_Status.objects.get(status = 'Ready For Pickup'))
    
    for r in repairs:
      email_list = []
      email_list.append(str(r.customer.email))
      message_body = 'Hello ' + str(r.customer.first_name) + ', Your Repair for your ' + str(r.repair_item) + ' is ready for pickup. To pickup and pay for your repair please bring this pickup ticket with you. Your Repair Ticket #:' + str(r.id)  
      
      # try:     
      send_mail('Your Repair is Ready!', message_body, 'austen@byuisys.com', 
        email_list, fail_silently=False)
      #except Exception:
        #print('Email Send Failed')
    
    tvars = {
      'repairs': repairs,
    }
      
    return templater.render_to_response(request, 'email_repairs_ready.html', tvars)
    #return HttpResponseRedirect("/manage/repairs/")
  
  else:
      return HttpResponseRedirect("/account/please_sign_in/")

    



  

  
