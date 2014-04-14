from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test


def process_request(request):
  if request.user.is_authenticated():
    '''Shows all Users in the DB'''

    # Get the user object 
    user = amod.User.objects.get(id = request.user.id)
  

    tvars = {
      'user': user,
    }
    return templater.render_to_response(request, 'my_account.html', tvars)
  
  else:
    return HttpResponseRedirect("/account/please_sign_in/")
  
  
