from django.shortcuts import render


# Create your views here.

#function for render form html page 
def home(request):
    return render(request,'Atlas_app/home.html')

#function for render datatable html page 
def datatable(request):
    return render(request,'Atlas_app/datatable.html')
