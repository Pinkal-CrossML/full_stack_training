from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    # path('cnnmodel',views.cnnmodel,name='cnnmodel'), #url for form page 
    
   
]
