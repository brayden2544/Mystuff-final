from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater


def process_request(request):
    # Get the Specific category from the url
    url_request = request.urlparams[0]
    
    # Filter all the products and get only the requested category
    products = mmod.Catalog_Item.objects.filter(category= url_request)
    category = mmod.Category.objects.get(id=url_request)

    tvars = {
      'products': products,
      'category': category,
    }
    return templater.render_to_response(request, 'category.html', tvars)
  
