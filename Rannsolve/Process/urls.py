from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.process,name='process'),
    path('cnnmodel',views.cnnmodel,name='cnnmodel'), #url for form page 
   
]
