from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
    '''Shows all Users in the DB'''
    users = amod.User.objects.exclude(is_active= False).order_by('id')
    
    title = 'Active MyStuff Users'

    tvars = {
      'users': users,
      'title': title,
    }
    return templater.render_to_response(request, 'users.html', tvars)
  
  else:
    return HttpResponseRedirect("/account/please_sign_in/")
  
@user_passes_test(lambda u: u.is_superuser)  
def process_request__staff(request):
  if request.user.is_authenticated():
    '''Shows all Users in the DB'''
    users = amod.User.objects.filter(is_staff = True).order_by('id')
    
    title = 'Active MyStuff Staff'

    tvars = {
      'users': users,
      'title': title,
    }
    return templater.render_to_response(request, 'users.html', tvars)
  
  else:
    return HttpResponseRedirect("/account/please_sign_in/")