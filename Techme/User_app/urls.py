from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('/register', views.Registeruser.as_view(),name='register'),
    path('/login_user', views.login_user,name='login_user')
]