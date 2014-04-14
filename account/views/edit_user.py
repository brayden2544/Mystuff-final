from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  '''Edits a single user'''
  user = amod.User.objects.get(id=request.urlparams[0])
  
  
  form = EditUserForm(initial={
    'username': user.username,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'email': user.email,
    'address': user.address,
    'city': user.city,
    'state': user.state,
    'zip_code': user.zip_code,
    'is_active': user.is_active,
    'is_superuser': user.is_superuser,
    'is_staff': user.is_staff,

  })
  
  if request.method == 'POST':
    form = EditUserForm(request.POST)
    if form.is_valid():
      user.username = form.cleaned_data['username']
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      user.address = form.cleaned_data['address']
      user.email = form.cleaned_data['email']
      user.city = form.cleaned_data['city']
      user.state = form.cleaned_data['state']
      user.zip_code = form.cleaned_data['zip_code']
      user.is_active= form.cleaned_data['is_active']
      user.is_superuser = form.cleaned_data['is_superuser']
      user.is_staff = form.cleaned_data['is_staff']
      user.save()
      
     
      
      return HttpResponseRedirect('/catalog/')
 
  tvars = {
    'form': form,
  }
  return templater.render_to_response(request, 'edit_user.html', tvars)

# Creates a new user and then redirects the user onto the Edit Store page using its new id
def process_request__new(request):
    new_user = amod.User() 
    if new_user.username != None:
      new_user.save()
      return HttpResponseRedirect('/account/edit_user/' + str(new_user.id) + '/')
    else:
      return HttpResponseRedirect('/account/users/')
    
def process_request__deactivate(request):
    user = amod.User.objects.get(id=request.urlparams[0])
    user.is_active = False
    user.save()
    return HttpResponseRedirect('/account/users/')
  
# The variables that will be put on the form
class EditUserForm(forms.Form):
  username= forms.CharField()
  first_name= forms.CharField()
  last_name= forms.CharField()
  email= forms.EmailField()
  address= forms.CharField()
  city= forms.CharField()
  state= forms.CharField()
  zip_code= forms.CharField()
  is_active= forms.BooleanField()
  is_superuser= forms.NullBooleanField()
  is_staff= forms.NullBooleanField()
  

  