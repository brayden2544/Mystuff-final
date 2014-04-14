from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from manage import models as mmod
from account import models as amod

class Transaction(models.Model):
    #ID
    user = models.ForeignKey(amod.User)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True)
    month = models.CharField(max_length=200, blank=True, null=True)

class Comission(Transaction):
    comission_period = models.CharField(max_length=200, blank=True, null=True) 
    employee = models.ForeignKey(amod.Employee, blank=True, null=True)
    comission_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Repair(models.Model):
    start_date = models.DateField(blank=True, null=True)
    expected_finish = models.DateField(blank=True, null=True)
    work_description = models.CharField(max_length=500, blank=True, null=True)
    hours = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employee = models.ForeignKey(amod.Employee)
    date_returned = models.DateField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  
  
  
  

  



 
  