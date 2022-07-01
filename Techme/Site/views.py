from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

#function for render form html page 
def home(request):
    return render(request,'Site/home.html')