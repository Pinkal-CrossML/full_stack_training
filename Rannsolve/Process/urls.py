from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.process,name='process'),
    path('cnnmodel',views.cnnmodel,name='cnnmodel'), #url for form page 
    path('add_process',views.add_process,name='add_process'), #url for form page 
    path('add_cnn_model',views.add_cnn_model,name='add_cnn_model'), #url for form page 
   
]
