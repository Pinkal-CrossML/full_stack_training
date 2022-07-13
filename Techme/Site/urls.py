from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('store',views.store,name='store'),
    path('cart',views.cart,name='cart'),
    path('product3',views.product,name='product3'),
    path('news',views.news,name='news'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    # path('cnnmodel',views.cnnmodel,name='cnnmodel'), #url for form page 
    
   
]
