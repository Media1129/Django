from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# from products.models  import Product
from home.models import User,UserInfo
from django.http import JsonResponse


# Create your views here.
def home_view(request,*args,**kwargs):
    # product_list = Product.objects.all()
    return render(request,"base.html",{})
    # return HttpResponse("<h1>Hello World Test</h1>")
def contact_view(request,*args, **kwargs):
    return render(request,"base.html",{})

def createUser_view(request):
    u = User.objects.create(name="lisa")
    # u.save()
    ui = UserInfo.objects.create(user_id=u, age=23)
    # ui.save()
    return render(request,"base.html",{})
    # return render(request,"home.html",{"state":"success"})
    # return JsonResponse({"state":"success"})

def getUser_view(request):
    U = User.objects.all()
    nameList = []
    for user in U:
        nameList.append(user.name)
    return render(request,"home.html",{"post_list":nameList})    
    # return JsonResponse({"userList": nameList})

    