from django.shortcuts import render
from .models import Process_data,Cnn_model
from Process.forms import Process_dataForm,Cnn_modelForm

# Create your views here.

#function for render form html page 
def process(request):
    form=Process_dataForm()
    return render(request,'process/process.html',{'form':form})


def cnnmodel(request):
    form=Cnn_modelForm()
    return render(request,'process/cnnmodel.html',{'form':form})

def add_process(request):
    form=Process_dataForm()
    if request.method == "POST":
        form = Process_dataForm(request.POST)
        if form.is_valid():
            form.save()

    # data = Cnn_model()
    # data.pipeline = request.POST.get('pipeline')
    # data.classification_model = request.POST.get('classification_model')
    # data.time_zone = request.POST.get('time_zone')
    # data.process_sla = request.POST.get('process_sla')
    # data.pre_processing = request.POST.get('pre_processing')
    # data.process_name = request.POST.get('process_name')
    # data.save()

        return render(request,'process/process.html',{'form':form})


def add_cnn_model(request):
    form=Cnn_modelForm()
    if request.method == "POST":
        form = Cnn_modelForm(request.POST)
        if form.is_valid():
            form.save()

        # data = Cnn_model()
        # data.type = request.POST.get('type')
        # data.activation = request.POST.get('activation')
        # data.name = request.POST.get('name')
        # data.test_size = request.POST.get('test_size')
        # data.epochs = request.POST.get('epochs')
        # data.Batch = request.POST.get('Batch')
        # data.kernel_Initializer = request.POST.get('kernel_Initializer')
        # data.cofidence_number = request.POST.get('cofidence_number')
        # data.optimize = request.POST.get('optimize')
        # data.save()
        
        return render(request,'process/cnnmodel.html',{'form':form})