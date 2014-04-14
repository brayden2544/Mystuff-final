from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth.tokens import default_token_generator
import datetime
from django.core.mail import EmailMultiAlternatives
import string
import random


def process_request(request):
   '''Creates a reset password form to email a unique link to the user'''
  
   form = PasswordResetForm()
  
   if request.method == 'POST':
       form = PasswordResetForm(request.POST)
        
       if form.is_valid():
           '''Get the email from the form and add it to the "To:" list'''
           email = form.cleaned_data['email']
           to    = []
           to.append(email)
            
           '''Generate a unique token to send to the user'''
           user                     = amod.User.objects.get(email=email)
           key                      = key_generator()
           user.password_reset_key  = key
           user.password_reset_date = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
           user.save()
   
           '''Create the email, open a connection, send the email, close the connection'''
           link = 'http://byuisys.com/account/reset_password/' + email + '/' + key + '/' 
           subject, from_email, to = 'MyStuff - Password Reset', 'admin@byuisys.com', email
           text_content = 'Hello! You\'ve requested to reset your MyStuff password. To choose a new password, follow this link: http://byuisys.com/account/reset_password/' + email + '/' + key + '/'
           html_content = '<p>Hello! You\'ve requested to reset your MyStuff password.</p><p>To choose a new password, follow this link: <a href="' + link + '"''>Reset Password</a><br><p>If you did not request a new password, please ignore this message.</p>'
           msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
           msg.attach_alternative(html_content, "text/html")
           msg.send()
        
           return HttpResponseRedirect('/account/reset_email_sent/')
 
   tvars = {
       'form': form,
   }
   return templater.render_to_response(request, 'forgot_password.html', tvars)
   
def key_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
  
class PasswordResetForm(forms.Form):
    email = forms.CharField()

    def clean_email(self):
      email = self.cleaned_data.get('email')
      if not amod.User.objects.filter(email=email):
          raise forms.ValidationError('No user account with that email. Are you sure you\'ve registered?')
      return email