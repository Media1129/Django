from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})
    # return HttpResponse("<h1>Hello World Test</h1>")
def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")
