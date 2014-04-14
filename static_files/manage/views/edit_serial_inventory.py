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
      inventory = mmod.Serial_Inventory.objects.get(id=request.urlparams[0])
  
  
      form = EditPhysicalInventoryForm(initial={
        'sku': inventory.sku,
        'category': inventory.category,
        'brand': inventory.brand,
        'description': inventory.description,
        'price': inventory.price,
        'serial': inventory.serial,
        'store_location': inventory.store_location,
        'shelf_location': inventory.shelf_location,
        'date_purchased': inventory.date_purchased,
        'comission_rate': inventory.comission_rate,

      })
  
      if request.method == 'POST':
        form = EditPhysicalInventoryForm(request.POST)
        if form.is_valid():
          inventory.sku = form.cleaned_data['sku']
          inventory.category = form.cleaned_data['category']
          inventory.brand = form.cleaned_data['brand']
          inventory.description = form.cleaned_data['description']
          inventory.price = form.cleaned_data['price']
          inventory.serial = form.cleaned_data['serial']
          inventory.store_location = form.cleaned_data['store_location']
          inventory.shelf_location = form.cleaned_data['shelf_location']
          inventory.date_purchased = form.cleaned_data['date_purchased']
          inventory.comission_rate = form.cleaned_data['comission_rate']
          inventory.save()
          return HttpResponseRedirect('/manage/physical_inventory/')
 
      tvars = {
        'form': form,
      }
      return templater.render_to_response(request, 'edit_serial_inventory.html', tvars)
      
  else:
      return HttpResponseRedirect("/account/please_sign_in/")

# Creates a new inventory and then redirects the user onto the Edit Inventory page using its new id
def process_request__new(request):
  new_inventory = mmod.Physical_Inventory()
  new_inventory.category_id = 1
  new_inventory.save()
  return HttpResponseRedirect('/manage/edit_serial_inventory/' + str(new_inventory.id) + '/')

# Creates a new inventory and then redirects the user onto the Edit Inventory page using its new id
def process_request__deactivate(request):
  inventory = mmod.Physical_Inventory.objects.get(id=request.urlparams[0])
  inventory.active = False
  inventory.save()
  return HttpResponseRedirect('/manage/serial_inventory/')

# The variables that will be put on the form
class EditPhysicalInventoryForm(forms.Form):
  sku= forms.CharField(required=False)
  category= forms.ModelChoiceField(queryset= mmod.Category.objects.all())
  brand= forms.CharField()
  description= forms.CharField()
  price= forms.CharField()
  serial= forms.CharField()
  store_location= forms.CharField()
  shelf_location= forms.CharField()
  date_purchased= forms.DateField(required=False)
  comission_rate= forms.CharField()
      
  

  
  
  