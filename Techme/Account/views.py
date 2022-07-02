from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

#function for render form html page 
def register(request):
    return render(request,'Account/register.html')

def login(request):
    return render(request,'Account/login.html')

def contact(request):
    return render(request,'Account/contact.html')