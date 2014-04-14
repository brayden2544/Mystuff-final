from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
   ## Attributes inherited from AbstractUser
   # username
   # first_name
   # last_name
   # email
   # password
   # is_active
   # is_staff
   # is_superuser
   # last_login
   # date_joined
   
   #Will use numeric ID for user id defined by the Database

    address = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    password_reset_key = models.CharField(max_length=20, blank=True, null=True)
    password_reset_date = models.DateTimeField(blank=True, null=True) 


class Employee(User):
   hire_date = models.DateField(blank=True, null=True)
   is_terminated = models.BooleanField(default=False)
   salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
   
class Membership(models.Model):
   user = models.ForeignKey(User)
   credit_card_number = models.CharField(max_length=200, blank=True, null=True)
   start_date = models.DateField(blank=True, null=True)
   end_date = models.DateField(blank=True, null=True)
   is_trial = models.BooleanField(default=False)



    
  
  
