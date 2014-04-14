from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
      '''Edits a single question'''
      store = mmod.Store.objects.get(id=request.urlparams[0])
  
  
      form = EditStoreForm(initial={
        'store_number': store.store_number,
        'location_name': store.location_name,
        'street': store.street,
        'city': store.city,
        'state': store.state,
        'zip_code': store.zip_code,
        'phone': store.phone,
        'hours': store.hours,

      })
  
      if request.method == 'POST':
        form = EditStoreForm(request.POST)
        if form.is_valid():
          store.store_number = form.cleaned_data['store_number']
          store.location_name = form.cleaned_data['location_name']
          store.street = form.cleaned_data['street']
          store.city = form.cleaned_data['city']
          store.state = form.cleaned_data['state']
          store.zip_code = form.cleaned_data['zip_code']
          store.phone = form.cleaned_data['phone']
          store.hours = form.cleaned_data['hours']
          store.save()
          return HttpResponseRedirect('/manage/stores')
 
      tvars = {
        'form': form,
      }
      
      return templater.render_to_response(request, 'edit_stores.html', tvars)
 
  else:
    return HttpResponseRedirect("/account/please_sign_in/")


# Creates a new store and then redirects the user onto the Edit Store page using its new id
def process_request__new(request):
  new_store = mmod.Store()
  new_store.save()
  return HttpResponseRedirect('/manage/edit_stores/' + str(new_store.id) + '/')
  
def process_request__deactivate(request):
  store = mmod.Store.objects.get(id=request.urlparams[0])
  store.active = False
  store.save()
  return HttpResponseRedirect('/manage/stores/')

# The variables that will be put on the form
class EditStoreForm(forms.Form):
  store_number= forms.CharField()
  location_name= forms.CharField()
  street= forms.CharField()
  city= forms.CharField()
  state= forms.CharField()
  zip_code= forms.CharField()
  phone= forms.CharField()
  hours= forms.CharField()
    


  
  
  