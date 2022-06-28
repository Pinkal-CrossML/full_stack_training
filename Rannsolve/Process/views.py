from django.shortcuts import render
from .models import Process_data,Cnn_model
from Process.forms import Process_dataForm,Cnn_modelForm
from django.contrib.auth.models import User

# Create your views here.

#function for render form html page 
def process(request):
    form=Process_dataForm()
    return render(request,'process/process.html',{'form':form})


def cnnmodel(request):
    form=Cnn_modelForm()

    cnn_data = Cnn_model.objects.all()
    data={
        'cnn_data':cnn_data,
        'form':form
    }
    return render(request,'process/cnnmodel.html',data)

def add_process(request):
    form=Process_dataForm()
    if request.method == "POST":
        form = Process_dataForm(request.POST)
        if form.is_valid():
            form.save()

        data = User()
        data.username = request.POST.get('user_id')
        data.password = request.POST.get('password')
        data.first_name = request.POST.get('first_name')
        data.email = request.POST.get('email')
        data.last_name = request.POST.get('last_name')
        data.save()

        return render(request,'process/process.html',{'form':form})


def add_cnn_model(request):
    form=Cnn_modelForm()
    print(request.FILES['sample_file'])
    cnn_data = Cnn_model.objects.all()
    
    if request.method == "POST" and request.FILES['sample_file']:

        form = Cnn_modelForm(request.POST)
        data={
        'cnn_data':cnn_data,
        'form':form
    }
        # breakpoint()
        if form.is_valid():
            
            my_model = form.save(commit=False)
            my_model.sample_file = request.FILES['sample_file']
            my_model.cnnclass = "Single Class"
            my_model.save()
            # breakpoint()
            # form.save()

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
        
        return render(request,'process/cnnmodel.html',data)

