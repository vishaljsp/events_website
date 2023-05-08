from django.shortcuts import render
from .models import *
import random
from .otp import*
from django.contrib.auth.models import User 


# Create your views here.


def home(request):
    productlider = Products.objects.filter(product_status="Publish")
    slidermn = Sliders.objects.all()
    if request.method=="POST":
        otpfn=random.randint(0,1000000)
        print("thi is otp",otpfn)
        nums=request.POST.get("num")
        smssender(nums,otpfn)
        if otpfn==otpfn:
            nm=User(username=nums,password=otpfn)
            nm.save()
            request.session["phone"]=nums
            print(request.session)

        else:
            print("otp not good")
    
    data = {
        'slider_home': slidermn,
        'product_slider': productlider,
        # 'ctls':lls,
    }
    return render(request, "home.html", data)



def check(request):
    if request.session.has_key('phone'):
        phone=request.session["phone"]
        v1=User.objects.get(username=phone)
        print(v1)
        
        return render(request,"home.html",{"v":v1})
        
    
    

def mobilestor(request):
    main_cat=Mian_Catogory.objects.all()

    data = {
        'catt':main_cat
    }
    return render(request, 'mobile-phones-store.html', data)

def pro(request):

    main_cat=Mian_Catogory.objects.all()

    ct = request.GET.get("probrand")
    if ct:
        prd=Products.objects.filter(Sub_catogory=ct)
    else:
        prd=Products.objects.filter(product_status="Publish")
    
   
    data = { 
        'prod':prd,    
        'catt':main_cat,

    }
    return render(request,"mobilse.html",data)

def salle(request,pk):
    main_cat=Mian_Catogory.objects.all()
    sl_fpro=Products.objects.get(id=pk)
    pd=Imagess.objects.filter(product=pk)
 
    return render(request,"saleout.html",context={"sale_product":sl_fpro,'catt':main_cat,"promg":pd})



def checkout(request):
    return render(request,"checkeout.html")