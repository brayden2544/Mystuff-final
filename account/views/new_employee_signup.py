from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from account import models as amod


def process_request(request):
  '''Edits a single employee'''
  employee = amod.Employee()
  
  
  form = EditUserForm(initial={
    'username': employee.username,
    'first_name': employee.first_name,
    'last_name': employee.last_name,
    'email': employee.email,
    'password': employee.password,
    'address': employee.address,
    'city': employee.city,
    'state': employee.state,
    'zip_code': employee.zip_code,
    

  })
  
  if request.method == 'POST':
    form = EditUserForm(request.POST)
    if form.is_valid():
      employee.username = form.cleaned_data['username']
      employee.first_name = form.cleaned_data['first_name']
      employee.last_name = form.cleaned_data['last_name']
      employee.set_password(form.cleaned_data['password'])
      employee.address = form.cleaned_data['address']
      employee.city = form.cleaned_data['city']
      employee.state = form.cleaned_data['state']
      employee.zip_code = form.cleaned_data['zip_code']
      employee.is_active= True
      employee.is_superuser = False
      employee.is_staff = True
      employee.save()
      return HttpResponseRedirect('/catalog/index/')
 
  tvars = {
    'form': form,
  }
  return templater.render_to_response(request, 'new_employee_signup.html', tvars)


    
  
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
  
def clean_employeename(self):
  employeename = self.cleaned_data.get('employeename')
  if employee.username and amod.User.objects.filter(username=employee.username).count() > 0:
    raise forms.ValidationError('This User Name is already registered.')
  return username

  

  