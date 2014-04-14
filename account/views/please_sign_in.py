from django import forms
from django.conf import settings
import django.contrib.auth
import django.contrib.contenttypes
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth import authenticate, login, logout



def process_request(request):

  form = LoginForm()
  if request.method == "POST":
    form =  LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      if user != None:
        login(request, user)
        return HttpResponseRedirect("/manage/index/")
  tvars = {
	  'form': form,
	}  
  
  return templater.render_to_response(request, 'please_sign_in.html', tvars)
  
  
class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())
   
  def clean(self):
    user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    if user == None:
      raise forms.ValidationError("Username or Password Incorrect. Please try again")
    return self.cleaned_data
    
def process_request__logout(request):
  logout(request)
  return HttpResponseRedirect("/manage/index/")