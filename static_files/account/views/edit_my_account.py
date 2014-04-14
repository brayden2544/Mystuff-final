from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout


def process_request(request):
  '''Edits a single user'''
  user = amod.User.objects.get(id=request.urlparams[0])
  
  
  form = EditUserForm(initial={
    'first_name': user.first_name,
    'last_name': user.last_name,
    'email': user.email,
    'address': user.address,
    'city': user.city,
    'state': user.state,
    'zip_code': user.zip_code,

  })
  
  if request.method == 'POST':
    form = EditUserForm(request.POST)
    if form.is_valid():
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      user.address = form.cleaned_data['address']
      user.email = form.cleaned_data['email']
      user.city = form.cleaned_data['city']
      user.state = form.cleaned_data['state']
      user.zip_code = form.cleaned_data['zip_code']
      user.save()
      return HttpResponseRedirect('/account/my_account/')
 
  tvars = {
    'form': form,
  }
  return templater.render_to_response(request, 'edit_user.html', tvars)


# Not Sure if I want to keep this for the user to be able to do or not    
def process_request__deactivate(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return HttpResponseRedirect('/catalog/')
  
# The variables that will be put on the form
class EditUserForm(forms.Form):
  first_name= forms.CharField()
  last_name= forms.CharField()
  email= forms.EmailField()
  address= forms.CharField()
  city= forms.CharField()
  state= forms.CharField()
  zip_code= forms.CharField()

  

  