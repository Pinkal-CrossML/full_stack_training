from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
<<<<<<< HEAD
    path('about',views.about,name='about'),
    path('store',views.store,name='store'),
=======
>>>>>>> 9f5e5efaf5b1897da2d6076c44fa44013844b621
    # path('cnnmodel',views.cnnmodel,name='cnnmodel'), #url for form page 
    
   
]
