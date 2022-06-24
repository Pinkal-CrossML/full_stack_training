from django import forms
from Process.models import Process_data,Cnn_model



class Process_dataForm(forms.ModelForm):
    class Meta:
        model = Process_data
        fields = '__all__'

class Cnn_modelForm(forms.ModelForm):
    class Meta:
        model = Cnn_model
        exclude = ["cnnclass", "sample_file"]