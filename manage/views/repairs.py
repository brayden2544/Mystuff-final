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
    '''Shows all questions in the DB'''
    repairs = mmod.Repair_Item.objects.exclude(returned=True)
  

    template_vars = {
      'repairs': repairs,
    }
    return templater.render_to_response(request, 'repairs.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
def process_request__delete(request): 
  repair = mmod.Repair_Item.objects.get(id=request.urlparams[0]) 
  repair.delete()
  return HttpResponseRedirect("/manage/repairs/")
  
  
  

  
