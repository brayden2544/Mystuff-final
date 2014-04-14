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
      item = mmod.Catalog_Item.objects.get(id=request.urlparams[0])
  
  
      form = EditCatalogItemsForm(initial={
        'sku': item.sku,
        'category': item.category,
        'brand': item.brand,
        'description': item.description,
        'price': item.price,

      })
  
      if request.method == 'POST':
        form = EditCatalogItemsForm(request.POST)
        if form.is_valid():
          item.sku = form.cleaned_data['sku']
          item.category = form.cleaned_data['category']
          item.brand = form.cleaned_data['brand']
          item.description = form.cleaned_data['description']
          item.price = form.cleaned_data['price']
          item.save()
          return HttpResponseRedirect('/manage/catalog_items')
 
      tvars = {
        'form': form,
      }
      return templater.render_to_response(request, 'edit_catalog_items.html', tvars)
  else:
      return HttpResponseRedirect("/account/please_sign_in/")

# Creates a new item and then redirects the user onto the Edit Inventory page using its new id
def process_request__new(request):
  new_item = mmod.Catalog_Item()
  new_item.category_id = 1
  new_item.brand_id = 1
  new_item.save()
  return HttpResponseRedirect('/manage/edit_catalog_items/' + str(new_item.id) + '/')

def process_request__deactivate(request):
  item = mmod.Catalog_Item.objects.get(id=request.urlparams[0])
  item.active = False
  item.save()
  return HttpResponseRedirect('/manage/catalog_items/')
    
  
# The variables that will be put on the form
class EditCatalogItemsForm(forms.Form):
  sku= forms.CharField()
  category= forms.ModelChoiceField(queryset= mmod.Category.objects.all())
  brand= forms.ModelChoiceField(queryset= mmod.Brand.objects.all())
  description= forms.CharField()
  price= forms.CharField()
      
  


  
  
  