from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from account import models as amod
from catalog import models as cmod
from . import templater
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import datetime

@user_passes_test(lambda u: u.is_staff)
def process_request(request):
   '''Prepares forms for shipping and billing addresses for checking out a cart'''
   
   if not request.user.is_authenticated():
       return HttpResponseRedirect('/account/login/')
   
   date = datetime.datetime.now()
   day = date.day
   month = date.strftime('%B')
   year = date.year
   monthYear = (str(month) + ' ' + str(year))
   dayMonthYear = (str(day) + ' ' + str(month) + ' ' + str(year))   
   
   employee = request.user

   form = ShippingForm(initial={
       'employee_id': employee.id,

   })
   
   if request.method == 'POST':
       form = ShippingForm(request.POST)
       if form.is_valid():
           
           #Get Cart information
           cart = request.session.get('cart', {})
           
           
           cart_items = []
           subtotal = 0
           comission_subtotal = 0
   
           for i in cart:
               product_object = mmod.Catalog_Item.objects.get(id=i)
               current_count = product_object.product_count
               quantity = cart[i]
               product_object.product_count = (current_count - quantity)
               product_object.save()
               subtotal += product_object.price * quantity
               comission_subtotal += (subtotal * product_object.comission_rate)
            
           
           user = amod.User.objects.get(id = form.cleaned_data['user_id'])
           comission = cmod.Comission()
           comission.user = user
           comission.employee = amod.Employee.objects.get(id = form.cleaned_data['employee_id'])
           comission.date = dayMonthYear
           comission.month = monthYear
           comission.comission_period = monthYear
           comission.comission_amount = comission_subtotal
           comission.amount = subtotal
           comission.save()

           
           request.session['cart']={}
           return HttpResponseRedirect('/catalog/receipt/')

   tvars = {
       'form': form,
   }

   return templater.render_to_response(request, 'checkout.html', tvars)
   
   
class ShippingForm(forms.Form):
    user_id         = forms.IntegerField()
    cc_number       = forms.CharField(max_length=16)
    security_code   = forms.CharField(max_length=3)
    expiration_date = forms.CharField()
    employee_id = forms.IntegerField(required=False)
    