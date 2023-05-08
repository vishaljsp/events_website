from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('mobile-phones-store',views.mobilestor,name='mobile-phones-store'),
    path('pro',views.pro,name='pro'),
    path('check-out',views.checkout,name='check-out'),
    path('check',views.check,name='check'),
    path("sale/<int:pk>",views.salle,name="sale")

]
if settings.DEBUG:

   urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
