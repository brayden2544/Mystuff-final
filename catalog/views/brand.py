from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater


def process_request(request):
    # Get the Specific category from the url
    url_request = request.urlparams[0]
    brand_request = mmod.Brand.objects.get(id=url_request)

    
    # Filter all the products and get only the requested category
    products = mmod.Catalog_Item.objects.filter(brand= mmod.Brand.objects.get(id=url_request))

    tvars = {
      'products': products,
      'brand_request': brand_request,
    }
    return templater.render_to_response(request, 'brand.html', tvars)
  
