from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from account import models as amod


def process_request(request):
  '''Edits a single user'''
  user = amod.User()
  
  
  form = EditUserForm(initial={
    'username': user.username,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'email': user.email,
    'password': user.password,
    'address': user.address,
    'city': user.city,
    'state': user.state,
    'zip_code': user.zip_code,
    

  })
  
  if request.method == 'POST':
    form = EditUserForm(request.POST)
    if form.is_valid():
      user.username = form.cleaned_data['username']
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      user.set_password(form.cleaned_data['password'])
      user.address = form.cleaned_data['address']
      user.city = form.cleaned_data['city']
      user.state = form.cleaned_data['state']
      user.zip_code = form.cleaned_data['zip_code']
      user.email = form.cleaned_data['email']
      user.is_active= True
      user.is_superuser = False
      user.is_staff = False
      user.save()
      return HttpResponseRedirect('/catalog/index/')
 
  tvars = {
    'form': form,
  }
  return templater.render_to_response(request, 'new_user_signup.html', tvars)


    
  
# The variables that will be put on the form
class EditUserForm(forms.Form):
  username= forms.CharField()
  first_name= forms.CharField()
  last_name= forms.CharField()
  email= forms.EmailField()
  password= forms.CharField(widget=forms.PasswordInput)
  address= forms.CharField()
  city= forms.CharField()
  state= forms.CharField()
  zip_code= forms.CharField()
  
def clean_username(self):
  username = self.cleaned_data.get('username')
  if user.username and amod.User.objects.filter(username=user.username).count() > 0:
    raise forms.ValidationError('This username is already registered.')
  return username

  

  