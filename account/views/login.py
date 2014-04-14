from django import forms
from django.conf import settings
import django.contrib.auth
import django.contrib.contenttypes
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth import authenticate, login, logout
from ldap3 import Connection, Server, AUTH_ANONYMOUS, AUTH_SIMPLE



def process_request(request):

  form = LoginForm()
  if request.method == "POST":
    form =  LoginForm(request.POST)
    if form.is_valid():
      print("<-------------- LDAP AUTHENTICATION START ------------------------>")
      try:
        username = form.cleaned_data['username']
        user_pass = form.cleaned_data['password']
        s = Server('localhost', port=389)
        c = Connection(
            s, 
            user=username + '@byuisys.local', 
            password=user_pass, 
            auto_bind=True
            )
        print("LDAP AUTH SUCCESS!")
        login(request)
        return HttpResponse('<script>window.location.href="/catalog/index/";</script>')
      except:
        print("LDAP AUTH FAILED")
        print("<-------------- LDAP AUTHENTICATION END ------------------------>")  
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user.is_active == True:
          login(request, user)
          return HttpResponse('<script>window.location.href="/catalog/index/";</script>')
  tvars = {
	  'form': form,
	}  
  
  return templater.render_to_response(request, 'login.html', tvars)
  
  
class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())
   
  def clean(self):
    user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    if user == None:
      raise forms.ValidationError("Username or Password Incorrect.")
    return self.cleaned_data
    
def process_request__logout(request):
  logout(request)
  return HttpResponseRedirect("/catalog/")