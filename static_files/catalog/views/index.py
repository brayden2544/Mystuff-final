from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater


def process_request(request):

    
    
    # Filter all the products 
    products = mmod.Catalog_Item.objects.all()


    tvars = {
      'products': products,
    }
    return templater.render_to_response(request, 'index.html', tvars)
  
