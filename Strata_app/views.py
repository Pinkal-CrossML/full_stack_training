from django.shortcuts import render


# Create your views here.

#function for render form html page 
def home(request):
    return render(request,'Strata_app/home.html')


