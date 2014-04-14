from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater


def process_request(request):
    '''Shows all Users in the DB'''

    # Get All the categories
    categories = mmod.Category.objects.all()
  

    tvars = {
      'categories': categories,
    }
    return templater.render_to_response(request, 'categories.html', tvars)
  
