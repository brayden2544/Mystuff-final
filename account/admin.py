from django.db import models
from django.contrib import admin
from manage import models as amod

# register any models here
admin.site.register(amod.User)
