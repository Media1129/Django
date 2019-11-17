from django.contrib import admin

# Register your models here.
from .models import Product #add to the IP:port/admin/ to show the product
#.models is relative path
admin.site.register(Product)
