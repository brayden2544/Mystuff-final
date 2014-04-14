from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
import datetime


def process_request(request):
   '''Creates a reset password form to email a unique link to the user'''
   
   user     = amod.User.objects.get(email=request.urlparams[0])
   key      = request.urlparams[1]
   now      = datetime.datetime.utcnow()
   exp_date = user.password_reset_date.replace(tzinfo=None)
   
   if key != user.password_reset_key or now > exp_date:
       return HttpResponseRedirect('/account/password_reset_invalid')
  
   form = PasswordForm()
  
   if request.method == 'POST':
       form = PasswordForm(request.POST)
        
       if form.is_valid():
           password = form.cleaned_data['password']
           print(user)
           print(password)
           user.set_password(password)
           user.save()
           return HttpResponseRedirect('/account/password_reset/')
 
   tvars = {
       'form': form,
   }
   return templater.render_to_response(request, 'reset_password.html', tvars)

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
