from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from mysite import settings
from tastypie.api import Api
from mobile.api import Repair_ItemResource, Repair_StatusResource,UserResource, Catalog_ItemResource,CategoryResource, BrandResource

from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(Repair_ItemResource())
v1_api.register(Repair_StatusResource())
v1_api.register(UserResource())
v1_api.register(Catalog_ItemResource())
v1_api.register(CategoryResource())
v1_api.register(BrandResource())



# specific urls that go to exact functions
urls = [
    '',
    # the standard admnistrator for django
    url(r'^admin/', include(admin.site.urls)),
    # to add Rest API 
    url(r'^api/', include(v1_api.urls)),

]

# dynamic urls for just about anything - send to the central controller
urls.extend([
  # the base_app.controller handles every request - this line is the glue that connects Mako to Django
  url(r'^.*$', 'base_app.controller.route_request' ),

])

# this is the variable Django really wants
urlpatterns = patterns(*urls)

# set up the views for page not found and server errors
#handler404 = 'base.views.page_not_found_404.process_request'
#handler500 = 'base.views.server_error_500.process_request'