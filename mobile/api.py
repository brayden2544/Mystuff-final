#mobile/api.py
#For rest calls to mobile app through TastyPie
from tastypie.resources import ModelResource
from manage import models as mmod
from account import models as amod
from catalog import models as cmod
from tastypie import fields


#Class to give Repair Statuses to mobile app        
class Repair_StatusResource(ModelResource):
    
    class Meta:
        queryset=mmod.Repair_Status.objects.all()
        resource_name = 'repair_status'
 #Class to give Users to mobile app       
class UserResource(ModelResource):
    class Meta:
        queryset = amod.User.objects.all()
        resource_name = 'user'

        
class CategoryResource(ModelResource):
    class Meta:
        queryset=mmod.Category.objects.all()
        resource_name='category'
        

class BrandResource(ModelResource):
    class Meta:
        queryset=mmod.Brand.objects.all()
        resource_name='brand'
		
#Class to give Repair items to mobile app        
class Repair_ItemResource(ModelResource):
    status = fields.ForeignKey(Repair_StatusResource, 'status')
    customer = fields.ForeignKey(UserResource, 'customer')
    
    class Meta:
        queryset= mmod.Repair_Item.objects.all()
        resource_name = 'repair_item'
		
#Class to give Catalog Items to mobile app     
class Catalog_ItemResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')
    brand = fields.ForeignKey(BrandResource, 'brand')
    class Meta:
        queryset=mmod.Catalog_Item.objects.all()
        resource_name='catalog_item'