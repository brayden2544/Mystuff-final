from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater



def process_request(request):
    # Get the Specific category from the url
    url_request = request.urlparams[0]
    
    # Filter all the products and get only the requested category
    product = mmod.Catalog_Item.objects.get(sku=url_request)
    product_category = product.category.id
    products = mmod.Catalog_Item.objects.filter(category= product_category)
   

    tvars = {
      'product': product,
      'products': products,

    }
    return templater.render_to_response(request, 'product.html', tvars)
  
def process_request__add_to_cart(request):
    product = mmod.Catalog_Item.objects.get(id=request.urlparams[0])
    
    if 'cart' not in request.session:
        request.session['cart'] = {}
        print("cart created")
        
    cart = request.session.get('cart', {})
    product_id = str(product.id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    print("added to cart")
    request.session['cart'] = cart
    return HttpResponseRedirect('/catalog/cart/')

def process_request__add_rental_to_cart(request):
    product = mmod.Catalog_Item.objects.get(id=request.urlparams[0])
    rental_option = request.urlparams[1]
    
    if 'rental_cart' not in request.session:
        request.session['rental_cart'] = {}
        print("rental cart created")
        
    rental_cart = request.session.get('rental_cart', {})
    product_id = str(product.id)
    if product_id in rental_cart:
        rental_cart[product_id] = rental_option
    else:
        rental_cart[product_id] = rental_option
    print("rental added to cart")
    request.session['rental_cart'] = rental_cart
    return HttpResponseRedirect('/catalog/cart/')