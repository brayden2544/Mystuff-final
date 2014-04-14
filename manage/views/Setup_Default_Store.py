from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manage import models as mmod
from . import templater
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def process_request(request):
  '''Check for Authntication'''
  if request.user.is_authenticated():
    '''Shows all questions in the DB'''
    
    inventory = mmod.Inventory()
    inventory.account_name = 'Inventory'
    inventory.balance= 0
    inventory.id = 1
    inventory.save()
    
    cash = mmod.Cash()
    cash.account_name = 'Cash'
    cash.id = 1
    cash.balance = 45678.90
    cash.save()
    
    PrepaidServiceLiability = mmod.PrepaidServiceLiability()
    PrepaidServiceLiability.account_name = 'Prepaid Service Liability'
    PrepaidServiceLiability.balance = 0
    PrepaidServiceLiability.id = 1
    PrepaidServiceLiability.save()
    
    repair_status1 = mmod.Repair_Status()
    repair_status1.status = 'Checked In'
    repair_status1.save()
    
    repair_status2 = mmod.Repair_Status()
    repair_status2.status = 'Started'
    repair_status2.save()
    
    repair_status3 = mmod.Repair_Status()
    repair_status3.status = 'In Process'
    repair_status3.save()
    
    repair_status4 = mmod.Repair_Status()
    repair_status4.status = 'Error with repair please contact our Repair Department'
    repair_status4.save()
    
    repair_status5 = mmod.Repair_Status()
    repair_status5.status = 'Quality Check Almost Complete'
    repair_status5.save()
    
    repair_status6 = mmod.Repair_Status()
    repair_status6.status = 'Ready For Pickup'
    repair_status6.save()
    
    repair_status7 = mmod.Repair_Status()
    repair_status7.status = 'Payment Needed'
    repair_status7.save()
    
    repair_status8 = mmod.Repair_Status()
    repair_status8.status = 'Repair Complete'
    repair_status8.save()
    
    
    
    
    store1= mmod.Store()
    store1.active = True
    store1.store_number = 1
    store1.location_name = 'Provo'
    store1.street = '200 North 500 East'
    store1.city = 'Provo'
    store1.state = 'Utah'
    store1.zip_code = '84604'
    store1.phone = '(801)234-2244'
    store1.hours = '8AM to 5PM Monday to Saturday - Closed Sunday'
    store1.save()
    
    store2= mmod.Store()
    store2.active = True
    store2.store_number = 2
    store2.location_name = 'South Jordan'
    store2.street = '500 South 400 East'
    store2.city = 'South Jordan'
    store2.state = 'Utah'
    store2.zip_code = '84095'
    store2.phone = '(801)354-1522'
    store2.hours = '8AM to 5PM Monday to Saturday - Closed Sunday'
    store2.save()
    
    store3= mmod.Store()
    store3.active = True
    store3.store_number = 3
    store3.location_name = 'Orem'
    store3.street = '22 University Parkway'
    store3.city = 'Orem'
    store3.state = 'Utah'
    store3.zip_code = '84057'
    store3.phone = '(801)274-6736'
    store3.hours = '8AM to 5PM Monday to Saturday - Closed Sunday'
    store3.save()
    
    category1 = mmod.Category()
    category1.category_name = 'Cameras'
    category1.category_description = 'Digital and Film based cameras'
    category1.save()
  
    category2 = mmod.Category()
    category2.category_name = 'Accessories'
    category2.category_description = 'Accessories for Digital and Film based cameras'
    category2.save()
  
    category3 = mmod.Category()
    category3.category_name = 'Printers'
    category3.category_description = 'High Quality Photo Printers'
    category3.save()
  
    category4 = mmod.Category()
    category4.category_name = 'Storage'
    category4.category_description = 'Flash Based storage for digital cameras'
    category4.save()
  
    brand1 = mmod.Brand()
    brand1.brand_name='Canon'
    brand1.save()
  
    brand2 = mmod.Brand()
    brand2.brand_name='Nikon'
    brand2.save()
  
    brand3 = mmod.Brand()
    brand3.brand_name='Sony'
    brand3.save()
  
    brand4 = mmod.Brand()
    brand4.brand_name='Panasonic'
    brand4.save()
    
    brand5 = mmod.Brand()
    brand5.brand_name='Lowepro'
    brand5.save()
    
    brand6 = mmod.Brand()
    brand6.brand_name='Epson'
    brand6.save()
    
    brand7 = mmod.Brand()
    brand7.brand_name='SanDisk'
    brand7.save()
    
    product1 = mmod.Serial_Inventory()
    product1.sku = 1980124
    product1.product_name = 'Canon - EOS Rebel T3i DSLR w 18-55mm Lens - Black'
    product1.availability = 1
    product1.category = mmod.Category(id=1)
    product1.brand = mmod.Brand(id=1)
    product1.description = 'Canon EOS Rebel T3i DSLR Camera with 18–55mm Lens: Capture your next masterpiece with this Canon Rebel T3i, an easy-to-use compact DSLR that boasts plenty of features. The DIGIC 4 Image Processor and 18.0-megapixel CMOS Image Sensor provide optimal performance for superb still shots, while Full HD recording delivers incredible performance when shooting video. No matter your experience with DSLR cameras, the multitude of features and ease of operation gives you more creative options.' 
    product1.cost = 399.99
    product1.price = 599.99
    product1.serial = 'H6HD63JD8H'
    product1.store_location = mmod.Store(id=1)
    product1.shelf_location = 'Shelf 7 Top Middle'
    product1.comission_rate = .15
    product1.product_count = 34
    product1.rentable = True
    product1.daily_rent_rate = 6.50
    product1.save()
    
    product2 = mmod.Serial_Inventory()
    product2.sku = 4826999
    product2.product_name = 'Nikon - D3200 DSLR Camera with 18-55mm VR Lens - Black'
    product2.availability = 1
    product2.category = mmod.Category(id=1)
    product2.brand = mmod.Brand(id=2)
    product2.description = 'Nikon D3200 DSLR Camera with 18–55mm VR Lens: Ultra quiet and powerful, great for taking candid photos. Or shoot full 1080p HD videos at up to 30 fps. Preprogrammed with auto options or choose your own settings to customize your shot, this compact camera can go anywhere with you.' 
    product2.cost = 299.99
    product2.price = 499.99
    product2.serial = 'D83HHD88D'
    product2.store_location = mmod.Store(id=1)
    product2.shelf_location = 'Shelf 7 Bottom Middle'
    product2.comission_rate = .15
    product2.product_count = 244
    product2.rentable = True
    product2.daily_rent_rate = 8.50
    product2.save()

    product3 = mmod.Serial_Inventory()
    product3.sku = 1579271
    product3.product_name = 'Sony - Alpha a3000 Compact System Camera with 18-55mm Lens - Black'
    product3.availability = 1
    product3.category = mmod.Category(id=1)
    product3.brand = mmod.Brand(id=3)
    product3.description = 'Capture important moments with this Sony Alpha a3000 compact system camera that features a 20.1-megapixel APS-C CMOS sensor that allows you to shoot clear photos and striking high-definition videos.' 
    product3.cost = 154.99
    product3.price = 399.99
    product3.serial = 'JD7FHD88D'
    product3.store_location = mmod.Store(id=2)
    product3.shelf_location = 'Shelf 10 Top'
    product3.comission_rate = .15
    product3.product_count = 267
    product3.rentable = True
    product3.daily_rent_rate = 4.50
    product3.save()
    
    
    product4 = mmod.Bulk_Inventory()
    product4.sku = 8394069
    product4.product_name = 'Lowepro - Format 110 Camera Bag - Black'
    product4.availability = 1
    product4.category = mmod.Category(id=2)
    product4.brand = mmod.Brand(id=5)
    product4.description = 'Bring your camera and other equipment on the go with this Lowepro Format 110 LP36509 camera bag that features a detachable shoulder strap to provide carrying comfort. The polyester and nylon materials ensure lasting use.'
    product4.cost= 10.22
    product4.price = 20.99
    product4.store_location = mmod.Store(id=2)
    product4.shelf_location = 'Shelf 3 Bottom Left'
    product4.comission_rate = .05
    product4.product_count = 544
    product4.save()

    product5 = mmod.Bulk_Inventory()
    product5.sku = 1180538
    product5.product_name = 'Lowepro - Adventura Ultra Zoom 100 Camera Bag'
    product5.availability = 1
    product5.category = mmod.Category(id=2)
    product5.brand = mmod.Brand(id=5)
    product5.description = 'This shoulder bag is compatible with most ultrazoom digital cameras and features an adjust-to-fit design with a padded divider that is removable for larger cameras. Pockets provide space for memory cards and other accessories.' 
    product5.cost = 12.24
    product5.price = 17.99
    product5.store_location = mmod.Store(id=3)
    product5.shelf_location = 'Shelf 5 Bottom Left'
    product5.comission_rate = .05
    product5.product_count = 864
    product5.save()
    
    product6 = mmod.Serial_Inventory()
    product6.sku = 8776103
    product6.product_name = 'Canon - PIXMA iP100 Mobile Printer'
    product6.availability = 1
    product6.category = mmod.Category(id=3)
    product6.brand = mmod.Brand(id=1)
    product6.description = 'Capture important moments with this Sony Alpha a3000 compact system camera that features a 20.1-megapixel APS-C CMOS sensor that allows you to shoot clear photos and striking high-definition videos.' 
    product6.cost = 160.56
    product6.price = 179.99
    product6.serial = 'G88HJDJ8DJE'
    product6.store_location = mmod.Store(id=2)
    product6.shelf_location = 'Shelf 18 Top'
    product6.comission_rate = .15
    product6.product_count = 574
    product6.rentable = False
    product6.save()
    
    product7 = mmod.Serial_Inventory()
    product7.sku = 9318909
    product7.product_name = 'Epson - Artisan A50 Printer'
    product7.availability = 1
    product7.category = mmod.Category(id=3)
    product7.brand = mmod.Brand(id=6)
    product7.description = 'This versatile printer allows you to print high-definition photos and also to print your own images and text onto compatible CDs and DVDs.' 
    product7.cost = 142.22
    product7.price = 229.99
    product7.serial = '8DH37RJ8DJE'
    product7.store_location = mmod.Store(id=3)
    product7.shelf_location = 'Shelf 26 Middle'
    product7.comission_rate = .15
    product7.product_count = 244
    product7.rentable = False
    product7.save()
    
    product8 = mmod.Bulk_Inventory()
    product8.sku = 4957245
    product8.product_name = 'SanDisk - Ultra 16GB Secure Digital High Capacity '
    product8.availability = 1
    product8.category = mmod.Category(id=4)
    product8.brand = mmod.Brand(id=7)
    product8.description = 'This 8GB Secure Digital High Capacity memory card features a Class 4 speed performance rating for fast read/write times and a security feature for protecting copyrighted material.'
    product8.cost = 7.64
    product8.price = 14.99
    product8.store_location = mmod.Store(id=3)
    product8.shelf_location = 'Shelf 1 Bottom Left'
    product8.comission_rate = .05
    product8.product_count = 665
    product8.save()
    
    product9 = mmod.Bulk_Inventory()
    product9.sku = 9138514
    product9.product_name = 'SanDisk - 8GB Secure Digital High Capacity (SDHC) '
    product9.availability = 1
    product9.category = mmod.Category(id=4)
    product9.brand = mmod.Brand(id=7)
    product9.description = 'Store and transfer digital photos, videos and more with this SanDisk Ultra Secure Digital High Capacity (SDHC) UHS-I Class 10 memory card that features a 16GB capacity for expansive storage and Class 10 performance for fast read and write speeds.'
    product9.cost = 2.22
    product9.price = 9.99
    product9.store_location = mmod.Store(id=1)
    product9.shelf_location = 'Shelf 1 Bottom Left'
    product9.comission_rate = .05
    product9.product_count = 452
    product9.save()
    
    
    template_vars = {

    }
    return templater.render_to_response(request, 'Setup_Default_Store.html', template_vars)
    
  else:
      return HttpResponseRedirect("/account/please_sign_in/")
  
  
  
  

  
