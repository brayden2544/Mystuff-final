from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
import datetime


@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
    
    now = datetime.datetime.now()
    thirty_days_ago = now - datetime.timedelta(days=30)
    sixty_days_ago = now - datetime.timedelta(days=60)
    ninety_days_ago = now - datetime.timedelta(days=90)
    
    
    
    thirty = mmod.Rental.objects.filter(date_out__lte=thirty_days_ago).exclude(returned=True)
    sixty = mmod.Rental.objects.filter(date_out__lte=sixty_days_ago).exclude(returned=True)
    ninety = mmod.Rental.objects.filter(date_out__lte=ninety_days_ago).exclude(returned=True)
    
    
    
    for t in thirty:
      email_list = []
      email_list.append(str(t.customer.email))
      message_body = 'Hello ' + str(t.customer.first_name) + ', Your Rental of the  ' + str(t.rental_item.product_name) + 'is more than 30 Days overdue for return. Please return this repair as soon as you can.  Also please reference this return id when you come in. Your Return Ticket #:' + str(t.id)  
      
      # try:     
      send_mail('Your Rental is more than 30 Days Overdue!', message_body, 'austen@byuisys.com', 
        email_list, fail_silently=False)
      #except Exception:
        #print('Email Send Failed')
        
    for s in sixty:
      email_list = []
      email_list.append(str(s.customer.email))
      message_body = 'Hello ' + str(s.customer.first_name) + ', Your Rental of the  ' + str(s.rental_item.product_name) + 'is more than 60 Days overdue for return. Please return this repair as soon as you can.  Also please reference this return id when you come in. Your Return Ticket #:' + str(s.id)  
      
      # try:     
      send_mail('Your Rental is more than 60 Days Overdue!', message_body, 'austen@byuisys.com', 
        email_list, fail_silently=False)
      #except Exception:
        #print('Email Send Failed')
    
    for n in ninety:
      email_list = []
      email_list.append(str(n.customer.email))
      message_body = 'Hello ' + str(n.customer.first_name) + ', Your Rental of the  ' + str(n.rental_item.product_name) + 'is more than 90 Days overdue for return. Please return this repair as soon as you can.  Also please reference this return id when you come in. Your Return Ticket #:' + str(n.id)  
    
      # try:     
      send_mail('Your Rental is more than 90 Days Overdue!', message_body, 'austen@byuisys.com', 
        email_list, fail_silently=False)
      #except Exception:
        #print('Email Send Failed')
      
    
    tvars = {
      'thirty': thirty,
      'sixty': sixty,
      'ninety': ninety,
    }
      
    return templater.render_to_response(request, 'email_overdue_rentals.html', tvars)
    #return HttpResponseRedirect("/manage/repairs/")
  
  else:
      return HttpResponseRedirect("/account/please_sign_in/")

    



  

  
