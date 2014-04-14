from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test


def process_request(request):
      
  
      form = SearchForm()
      
  
      if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
          search = form.cleaned_data['search']
          '''return HttpResponse('<script>window.location.href="/manage/index/";</script>')'''
          return HttpResponse('<script> window.location.href="/catalog/search_results/" + str(search);</script>')
 
      tvars = {
        'form': form,
      }
      
      return templater.render_to_response(request, 'search.html', tvars)


  
# The variables that will be put on the form
class SearchForm(forms.Form):
  search= forms.CharField()