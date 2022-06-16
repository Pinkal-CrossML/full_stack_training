from django.shortcuts import render


# Create your views here.

#function for render form html page 
def process(request):
    return render(request,'process/process.html')


def cnnmodel(request):
    return render(request,'process/cnnmodel.html')