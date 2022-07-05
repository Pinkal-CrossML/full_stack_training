from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

#function for render form html page 
def home(request):
    return render(request,'Site/home.html')

def about(request):
    return render(request,'Site/about.html')

def store(request):
    return render(request,'Site/store.html')

def cart(request):
    return render(request,'Site/cart.html')

def product(request):
    return render(request,'Site/product.html')

def news(request):
    return render(request,'Site/news.html')

def services(request):
    return render(request,'Site/services.html')

def contact(request):
    return render(request,'Site/contact.html')