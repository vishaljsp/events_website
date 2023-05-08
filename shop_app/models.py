from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.contrib.auth.models import User 


from django.contrib.auth.models import AbstractUser


class Customeruser(AbstractUser):
    # genders=("Male","Male"),("Female","Female")
    otp=models.CharField(max_length=50)
    # gender=models.CharField(choices=genders,max_length=50)


    

class Brands(models.Model):
    brands = models.CharField(max_length=500)

    def __str__(self):



        return self.brands


class Mian_Catogory(models.Model):
    name=models.CharField(max_length=500,default=None)
    

    def __str__(self):
        return self.name



class Catogory(models.Model):
    mn_catogory = models.ForeignKey(Mian_Catogory,on_delete=models.CASCADE)
    name=models.CharField(max_length=500,default=None)

    def __str__(self):
        return self.name


class SubCatogory(models.Model):
    catogory = models.ForeignKey(Catogory,on_delete=models.CASCADE)
    name=models.CharField(max_length=500,default=None)

    def __str__(self):
        return self.name



class Sliders(models.Model):
    slider_image=models.ImageField(upload_to="media/slider/")
    slider_image_name=models.CharField(max_length=300)

class Products(models.Model):
    Pd_stock=("IN STOCK","IN STOCK"),("OUT OF STOCK"," OUT OF STOCK")
    Status=('Publish', 'Publish'),('Draft', 'Draft')
    
    Product_name=models.CharField(max_length=600)

    Products_image=models.ImageField(upload_to="media/product_image/")
    

    image_name=models.CharField(max_length=500)

    Product_price=models.IntegerField()

    product_info=models.TextField(max_length=1000)

    product_descreption=models.TextField(max_length=1000,blank=True)

    stock=models.CharField(choices=Pd_stock,max_length=300)

    date=models.DateField(default=timezone.now)

    product_status=models.CharField(choices=Status,max_length=300)

    offers=models.TextField(blank=True)
    catogory=models.ForeignKey(Mian_Catogory,on_delete=models.CASCADE)

    Main_catogory=models.ForeignKey(Catogory,on_delete=models.CASCADE)

    Sub_catogory=models.ForeignKey(SubCatogory,on_delete=models.CASCADE)
    
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)

    new_slug=AutoSlugField(populate_from="Product_name",unique=True,null=True,default=None)

    def __str__(self):
        return self.Product_name


class Phone_store(models.Model):
    image=models.ImageField(upload_to='media/phone_store/', max_length=500)
    image_name=models.CharField(max_length=500)

class Phone_store_images(models.Model):
    image=models.ImageField(upload_to='media/product_image/', max_length=500)
    image_name=models.CharField(max_length=500)
    product=models.ForeignKey(Phone_store,on_delete=models.CASCADE)


class Imagess(models.Model):
    image=models.ImageField(upload_to='media/product_image/', max_length=500)
    image_name=models.CharField(max_length=500)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)


