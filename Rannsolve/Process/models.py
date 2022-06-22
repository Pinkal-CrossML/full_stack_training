from unicodedata import name
from django.db import models

# Create your models here.


class Process_data(models.Model):
    pipeline_choices = (
        (0,'engine_1'),
        (1,'engine_2'),
        (2,'engine_3'),
        (4,'engine_4'),
    )
    pipeline = models.CharField(max_length=50, choices=pipeline_choices,null=True)

    classification_model_choices = (
        (1,'yes'),
        (0,'no'),
    )
    classification_model = models.CharField(max_length=50, choices=classification_model_choices,null=True)

    time_zone_choices = (
        (0,'usa'),
        (1,'in'),
        (2,'uk'),
    )
    time_zone = models.CharField(max_length=50, choices=time_zone_choices,null=True)

    process_sla_choices = (
        (0,'1'),
        (1,'2'),
        (2,'3'),
    )
    process_sla = models.CharField(max_length=50, choices=process_sla_choices,null=True)

    pre_processing_choices = (
        (0,'pre1'),
        (1,'pre2'),
        (2,'pre3'),
    )
    pre_processing = models.CharField(max_length=50, choices=pre_processing_choices,null=True)
    
    process_name = models.CharField(max_length=50)
    def __str__(self):
        return self.process_name