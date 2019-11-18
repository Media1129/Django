from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from products.models  import Product


# Create your views here.
def home_view(request,*args,**kwargs):
    product_list = Product.objects.all()
    return render(request,"home.html",{'post_list':product_list})
    # return HttpResponse("<h1>Hello World Test</h1>")
def contact_view(request,*args, **kwargs):
    return render(request,"base.html",{})
    