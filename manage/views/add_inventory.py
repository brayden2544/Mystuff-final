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
      current_product = mmod.Catalog_Item.objects.get(sku= request.urlparams[0])
      
      
      current_count = current_product.product_count
  
      form = EditInventoryForm()
  
      if request.method == 'POST':
        form = EditInventoryForm(request.POST)
        if form.is_valid():
          current_product.product_count = current_count + form.cleaned_data['amount_to_add']
          current_product.save()
          return HttpResponseRedirect('/manage/inventory/')
 
      tvars = {
        'form': form,
      }
      
      return templater.render_to_response(request, 'add_inventory.html', tvars)
 
  else:
    return HttpResponseRedirect("/account/please_sign_in/")


  
# The variables that will be put on the form
class EditInventoryForm(forms.Form):
  amount_to_add= forms.IntegerField()

    


  
  
  