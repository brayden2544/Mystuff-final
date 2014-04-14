from django.db import models
from account.models import User
from django.conf import settings
from django.utils import timezone
from account import models as amod

    
class Store(models.Model):
    active = models.BooleanField(default=True)
    store_number = models.IntegerField(default=0, blank=True, null=True)
    location_name = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    hours = models.CharField(max_length=200, blank=True, null=True)
    #manager = models.ForeignKey(User) will use later when I add the user class
    
    def __str__(self):
      return '%i: %s' % (self.id, self.location_name)
    
class Category(models.Model):
    category_name = models.CharField(max_length=200, blank=True, null=True)
    category_description = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
      return '%s' % (self.category_name)

class Brand(models.Model):
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
      return '%s' % (self.brand_name)

class Catalog_Item(models.Model):
    active = models.BooleanField(default=True)
    sku = models.CharField(max_length=200, blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    availability = models.IntegerField(max_length=3, blank=True, null=True) 
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    description = models.CharField(max_length=500, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    comission_rate = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    product_count = models.IntegerField(blank=True, null=True)
    rentable = models.BooleanField(default = False)
    daily_rent_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
      return '%s: %s' % (self.sku, self.product_name)
     
  
class Serial_Inventory(Catalog_Item):
    serial = models.CharField(max_length=200, blank=True, null=True)
    store_location = models.ForeignKey(Store)
    shelf_location = models.CharField(max_length=200, blank=True, null=True)
    date_purchased = models.DateTimeField(blank=True, null=True)


    def __str__(self):
      return '%s: %s' % (self.serial, self.product_name)

class Bulk_Inventory(Catalog_Item):
    store_location = models.CharField(max_length=200, blank=True, null=True)
    shelf_location = models.CharField(max_length=200, blank=True, null=True)
    
    
    def __str__(self):
      return '%s' % (self.product_name)


class Rental(models.Model):
     customer = models.ForeignKey(amod.User)
     rental_item = models.ForeignKey(Catalog_Item)
     date_out = models.DateField(auto_now=False, auto_now_add=False, null=True)
     expected_return = models.DateField(auto_now=False, auto_now_add=False, null=True)
     pre_condition = models.CharField(max_length=200, blank=True, null=True)
     date_returned = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
     post_condition = models.CharField(max_length=200, blank=True, null=True)
     total_days_late = models.IntegerField(blank=True, null=True)   
     late_fees = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
     damage_report = models.CharField(max_length=200, blank=True, null=True)
     damage_fees = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
     total_fees = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
     returned = models.BooleanField(default = False)

class Repair_Status(models.Model):
      status = models.CharField(max_length=200, blank=True, null=True)
      
      def __str__(self):
        return '%s' % (self.status)

class Repair_Item(models.Model):
     customer = models.ForeignKey(amod.User)
     repair_item = models.CharField(max_length=200, blank=True, null=True)
     date_in = models.DateField(auto_now=False, auto_now_add=False, null=True)
     expected_return = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
     issue = models.CharField(max_length=200, blank=True, null=True)
     status = models.ForeignKey(Repair_Status)
     damage_report = models.CharField(max_length=200, blank=True, null=True)
     date_returned = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
     repairs = models.CharField(max_length=200, blank=True, null=True)
     repair_fees = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
     returned = models.BooleanField(default = False)
     paid_for = models.BooleanField(default = False)
   
    
#Accounts 

class BalanceSheetAccounts(models.Model):
     account_name = models.CharField(max_length=200, blank=True, null=True)
     
class Inventory(BalanceSheetAccounts):  
     balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
     
class Cash(BalanceSheetAccounts):
     balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

class PrepaidServiceLiability(BalanceSheetAccounts):
     balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

class IncomeSheetAccounts(models.Model):
     account_name = models.CharField(max_length=200, blank=True, null=True)
     date = models.CharField(max_length=200, blank=True, null=True)
     
class Revenue(IncomeSheetAccounts):
     balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

class ComissionsExpense(IncomeSheetAccounts):
     balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

class SalesTaxPayable(IncomeSheetAccounts):
     balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
     







