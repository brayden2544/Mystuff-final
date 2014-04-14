from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth.decorators import user_passes_test


def process_request(request):
  '''Edits a single user'''
  user = amod.User.objects.get(id=request.user.id)
  
  form = EditUserForm()
  
  if request.method == 'POST':
    form = EditUserForm(request.POST)
    if form.is_valid():
      if form.cleaned_data['Password'] == form.cleaned_data['Password_Again']:
        user.set_password(form.cleaned_data['Password'])
        user.save()
        return HttpResponseRedirect('/account/my_account/')
      else:
        return HttpResponseRedirect('/account/my_account/')
 
  tvars = {
    'form': form,
  }
  return templater.render_to_response(request, 'edit_my_password.html', tvars)
  


  
# The variables that will be put on the form
class EditUserForm(forms.Form):
  Password= forms.CharField(widget=forms.PasswordInput)
  Password_Again= forms.CharField(widget=forms.PasswordInput)
  
  