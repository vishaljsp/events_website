from django.contrib import admin
from .models import *




class imagetublerinlain(admin.TabularInline):
    model=Imagess

class ProductsAdmin(admin.ModelAdmin):
    inlines=[imagetublerinlain] 

class Stor_image(admin.TabularInline):
    model=Phone_store_images

class P_stor(admin.ModelAdmin):
    inlines=[Stor_image]



admin.site.register(Customeruser)
admin.site.register(Phone_store,P_stor)
admin.site.register(Phone_store_images)
admin.site.register(Imagess)
admin.site.register(Sliders)
admin.site.register(Mian_Catogory)
admin.site.register(Brands)
admin.site.register(SubCatogory)
admin.site.register(Catogory)
admin.site.register(Products,ProductsAdmin)

