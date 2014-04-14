from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test


def process_request(request):
      
      search = request.urlparams[0]
  
      products = mmod.Catalog_Item.objects.filter(product_name__contains=search.lower())
 
      tvars = {
        'products': products,
        'search': search,
      }
      
      return templater.render_to_response(request, 'search_results.html', tvars)


  
# The variables that will be put on the form
class SearchForm(forms.Form):
  search= forms.CharField()