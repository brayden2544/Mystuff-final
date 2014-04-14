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
    '''Shows all questions in the DB'''
    
    now = datetime.datetime.now()
    thirty_days_ago = now - datetime.timedelta(days=30)
    sixty_days_ago = now - datetime.timedelta(days=60)
    ninety_days_ago = now - datetime.timedelta(days=90)
    
    
    
    thirty = mmod.Rental.objects.filter(date_out__lte=thirty_days_ago).exclude(returned=True)
    sixty = mmod.Rental.objects.filter(date_out__lte=sixty_days_ago).exclude(returned=True)
    ninety = mmod.Rental.objects.filter(date_out__lte=ninety_days_ago).exclude(returned=True)
    
  

    template_vars = {
      'thirty': thirty,
      'sixty': sixty,
      'ninety': ninety,
    }
    return templater.render_to_response(request, 'overdue_rental.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
  
  

  
