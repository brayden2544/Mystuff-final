from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
    '''Shows all questions in the DB'''
    item = mmod.Catalog_Item.objects.exclude(active=False).order_by('id')

    template_vars = {
      'item': item,
    }
    return templater.render_to_response(request, 'catalog_items.html', template_vars)

  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
