from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from account import models as amod
from catalog import models as cmod
from . import templater
from django.contrib.auth.decorators import login_required
import datetime
from decimal import Decimal
import requests
import simplejson
from django.core.mail import send_mail


@login_required
def process_request(request):
   '''Prepares forms for shipping and billing addresses for checking out a cart'''
   
   if not request.user.is_authenticated():
       return HttpResponseRedirect('/account/login/')
   
   date = datetime.datetime.now()
   day = date.day
   month = date.strftime('%B')
   month_num = date.strftime('%m')
   year = date.year
   monthYear = (str(month) + ' ' + str(year))
   dayMonthYear = (str(day) + ' ' + str(month) + ' ' + str(year))
   save_date = (str(month_num) + '/' + str(day) + '/' + str(year))   
   
   '''Balance Sheet Accounts'''
   cash_account = mmod.Cash.objects.get(id=1)
   current_cash_balance = cash_account.balance
   inventory_account = mmod.Inventory.objects.get(id=1)
   current_inventory_balance = inventory_account.balance
   
   cart = request.session.get('cart', {})
   rental_cart = request.session.get('rental_cart', {})
   repair_cart = request.session.get('repair_cart', {})
   
   cost_subtotal = 0
   subtotal = 0
   
   for i in cart:
       product_object = mmod.Catalog_Item.objects.get(id=i)
       current_count = product_object.product_count
       quantity = cart[i]
       product_object.product_count = (current_count - quantity)
       cost_subtotal += product_object.cost
       product_object.save()
       subtotal += product_object.price * quantity
  
   for r in rental_cart:
       product_object = mmod.Catalog_Item.objects.get(id=r)
       rental_option = Decimal(rental_cart[r])
       subtotal += product_object.daily_rent_rate * Decimal(rental_option)
   
   for a in repair_cart:
       repair = mmod.Repair_Item.objects.get(id=a)
       subtotal += repair.repair_fees
       
       

   
   amount =  subtotal
   cash_account.balance = (current_cash_balance + subtotal)
   cash_account.save()
   inventory_account.balance = (current_inventory_balance + cost_subtotal)
   inventory_account.save()
   user = amod.User.objects.get(id=request.user.id)

   form = ShippingForm(initial={
       'first_name': user.first_name,
       'last_name': user.last_name,
       'address': user.address,
       'city': user.city,
       'state': user.state,
       'zip_code': user.zip_code,
   })
   
   if request.method == 'POST':
       form = ShippingForm(request.POST)
       if form.is_valid():

           for r in rental_cart:
               product_object = mmod.Catalog_Item.objects.get(id=r)
               rental_option = int(rental_cart[r])
               rental = mmod.Rental()
               rental.customer = request.user
               rental.rental_item = product_object
               rental.date_out = save_date
               expected_return = date + datetime.timedelta(days=rental_option)
               e_day = expected_return.day
               e_month = expected_return.strftime('%m')
               e_year = expected_return.year
               rental.expected_return = (str(e_month)+ '/' + str(e_day) + '/' + str(e_year))
               rental.pre_condition = 'New'
               rental.save()
               message_body = 'Hello ' + str(t.customer.first_name) + ', Your Rental of the  ' + str(t.rental_item.product_name) + 'is more than 30 Days overdue for return. Please return this repair as soon as you can.  Also please reference this return id when you come in. Your Return Ticket #:' + str(t.id)
               
           for a in repair_cart:
             repair = mmod.Repair_Item.objects.get(id=a)
             repair.paid_for = True
             repair.save()
                   
               
           transaction = cmod.Transaction()
           transaction.user = user
           transaction.date = dayMonthYear
           transaction.month = monthYear
           transaction.amount = amount
           transaction.save()
           
           
           #Send request using rest call
           API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
           API_KEY = 'aa846fb6f04d54c4b952561399e40d84'
           r = requests.post(API_URL, data={
             'apiKey': API_KEY,
             'currency': 'usd',
             'amount': '5.99',
             'type': 'Visa',
             'number': '4732817300654',
             'exp_month': 10,
             'exp_year': 14,
             'cvc': 411,
             'name': 'Cosmo Limesandal',
             'description': 'Charge for cosmo@is411.byu.edu',
           })
           
           
           resp = r.json()
           
           id = (resp['ID'])
           amount = (resp['Amount'])
           description = (resp['Description'])
           
           
           email_list = []
           email_list.append(str(request.user.email))
           message_body = 'Hello ' + str(request.user.first_name) + ', Your purchase has been completed for: $' + str(transaction.amount) + '. Please save this Reciept for your Reference. Your Reciept ID is: ' + str(transaction.id)    
           send_mail('Your Reciept', message_body, 'austen@byuisys.com', 
             email_list, fail_silently=False)  
           
           
           
           rvars = {
              'id': id,
              'amount': amount,
              'description': description,
           }
           
           request.session['cart']={}
           request.session['rental_cart']={}
           request.session['repair_cart']= {}
           
           return templater.render_to_response(request, 'receipt.html', rvars)

   tvars = {
       'form': form,
   }

   return templater.render_to_response(request, 'checkout.html', tvars)
   
   
class ShippingForm(forms.Form):
    first_name      = forms.CharField()
    last_name       = forms.CharField()
    address         = forms.CharField()
    city            = forms.CharField()
    state           = forms.CharField()
    zip_code        = forms.CharField(max_length=5)
    cc_number       = forms.CharField(max_length=16)
    security_code   = forms.CharField(max_length=3)
    expiration_date = forms.CharField()
    