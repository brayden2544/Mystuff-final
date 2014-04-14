from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater


def process_request(request):

    
    # Filter all the products and get only the requested category
    products = mmod.Catalog_Item.objects.filter(rentable= True)

    tvars = {
      'products': products,
    }
    return templater.render_to_response(request, 'rentable.html', tvars)
  
