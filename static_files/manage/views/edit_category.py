from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  if request.user.is_authenticated():
      '''Edits a single question'''
      category = mmod.Category.objects.get(id=request.urlparams[0]) 
  
      form = EditCategoryForm(initial={
        'category_name': category.category_name,
        'category_description': category.category_description,

      })
  
      if request.method == 'POST':
        form = EditCategoryForm(request.POST)
        if form.is_valid():
          category.category_name = form.cleaned_data['category_name']
          category.category_description = form.cleaned_data['category_description']
          category.save()
          return HttpResponseRedirect('/manage/category/')
 
      tvars = {
        'form': form,
      }
      
      return templater.render_to_response(request, 'edit_category.html', tvars)
 
  else:
    return HttpResponseRedirect("/account/please_sign_in/")


# Creates a new store and then redirects the user onto the Edit Store page using its new id
def process_request__new(request):
  new_category = mmod.Category()
  new_category.save()
  return HttpResponseRedirect('/manage/edit_category/' + str(new_category.id) + '/')
  
# The variables that will be put on the form
class EditCategoryForm(forms.Form):
  category_name= forms.CharField()
  category_description= forms.CharField()

    


  
  
  