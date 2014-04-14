from django.db import models
from django.contrib import admin
from manage import models as mmod

# register any models here
admin.site.register(mmod.Store)
admin.site.register(mmod.Serial_Inventory)
admin.site.register(mmod.Catalog_Item)
admin.site.register(mmod.Brand)
admin.site.register(mmod.Category)
admin.site.register(mmod.Bulk_Inventory)
admin.site.register(mmod.Rental)
admin.site.register(mmod.Repair_Status)
admin.site.register(mmod.Repair_Item)
