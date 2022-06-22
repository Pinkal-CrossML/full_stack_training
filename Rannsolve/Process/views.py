from django.shortcuts import render
from .models import Process_data

# Create your views here.

#function for render form html page 
def process(request):
    return render(request,'process/process.html')


# def cnnmodel(request):
#     return render(request,'process/cnnmodel.html')

def add_process(request):
    if request.method == "POST":
        data = Process_data()
        data.pipeline = request.POST.get('pipeline')
        data.classification_model = request.POST.get('classification_model')
        data.time_zone = request.POST.get('time_zone')
        data.process_sla = request.POST.get('process_sla')
        data.pre_processing = request.POST.get('pre_processing')
        data.process_name = request.POST.get('process_name')
        data.save()
        return render(request,'process/process.html')
