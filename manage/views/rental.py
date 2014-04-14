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
    rental = mmod.Rental.objects.exclude(returned=True)
  

    template_vars = {
      'rental': rental,
    }
    return templater.render_to_response(request, 'rental.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
  
  

  
