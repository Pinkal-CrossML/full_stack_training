from unicodedata import name
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import FileExtensionValidator

# Create your models here.

class Process_data(models.Model):
    pipeline_choices = (
        ('Engine-1','engine_1'),
        ('Engine-2','engine_2'),
        ('Engine-3','engine_3'),
        ('Engine-4','engine_4'),
    )
    classification_model_choices = (
        ('Yes','yes'),
        ('No','no'),
    )

    time_zone_choices = (
        ('usa','usa'),
        ('in','in'),
        ('uk','uk'),
    )

    process_sla_choices = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    
    pre_processing_choices = (
        ('yes','yes'),
        ('no','no'),
       
    )
    Input_documents_choices = (
        ('JPG','JPG'),
        ('PDF','PDF'),
        ('JPEG','JPEG'),
        ('TIF','TIF'),
        ('PNG','PNG'),
       
    )

    Input_documents = MultiSelectField(choices=Input_documents_choices,null=True)
    pre_processing = models.CharField(max_length=50, choices=pre_processing_choices,null=True)
    pipeline = models.CharField(max_length=50, choices=pipeline_choices,null=True)
    classification_model = models.CharField(max_length=50, choices=classification_model_choices,null=True)
    time_zone = models.CharField(max_length=50, choices=time_zone_choices,null=True)
    process_sla = models.CharField(max_length=50, choices=process_sla_choices,null=True)

    process_name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.process_name



class Cnn_model(models.Model):
    type_coices = (
        ('Regular_Model','Regular_Model'),
        ('VCG_Model','VCG_Model'),
        
    )
    epochs_choices = (
        ('20','20'),
        ('30','30'),
        ('40','40'),
        ('50','50'),
        ('60','60'),
        ('70','70'),
        ('80','80'),
        ('90','90'),
        ('100','100'),
        
    )
    batch_choices = (
        ('16','16'),
        ('32','32'),
        ('64','64'),
        
    )
    kernel_Initializer_choices = (
        ('he_noraml','he_noraml'),
        ('he_uniform','he_uniform'),
        
    )
    optimize_choices = (
        ('rmsprop','rmsprop'),
        ('xrmprop','xrmprop'),
        
    )
    test_size_choices = (
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        
    )
    activation_choices = (
        ('relu','relu'),
        ('esl','esl'),
        
    )

    type = models.CharField(max_length=50, choices=type_coices,null=True)
    activation = models.CharField(max_length=50, choices=activation_choices,null=True)
    test_size = models.CharField(max_length=50, choices=test_size_choices,null=True)
    epochs = models.CharField(max_length=50, choices=epochs_choices,null=True)
    Batch = models.CharField(max_length=50, choices=batch_choices,null=True)
    kernel_Initializer = models.CharField(max_length=50, choices=kernel_Initializer_choices,null=True)
    optimize = models.CharField(max_length=50, choices=optimize_choices,null=True)
    cofidence_number = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    cnnclass = models.CharField(max_length=50,default="Single_Class")
    cv_file = models.FileField(null=True)
   
    def __str__(self):
        return self.name