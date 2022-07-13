from django.urls import path
from . import views
urlpatterns = [
    # path('category/', views.CategoryView.as_view()),
    path('/product1/', views.ProductView.as_view()),

]