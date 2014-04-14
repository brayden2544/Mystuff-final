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
      brand = mmod.Brand.objects.get(id=request.urlparams[0])
  
  
      form = EditBrandForm(initial={
        'brand_name': brand.brand_name,


      })
  
      if request.method == 'POST':
        form = EditBrandForm(request.POST)
        if form.is_valid():
          brand.brand_name = form.cleaned_data['brand_name']
          brand.save()
          return HttpResponseRedirect('/manage/brand')
 
      tvars = {
        'form': form,
      }
      
      return templater.render_to_response(request, 'edit_brand.html', tvars)
 
  else:
    return HttpResponseRedirect("/account/please_sign_in/")


# Creates a new store and then redirects the user onto the Edit Store page using its new id
def process_request__new(request):
  new_brand = mmod.Brand()
  new_brand.save()
  return HttpResponseRedirect('/manage/brand/' + str(new_brand.id) + '/')
  

# The variables that will be put on the form
class EditBrandForm(forms.Form):
  brand_name= forms.CharField()