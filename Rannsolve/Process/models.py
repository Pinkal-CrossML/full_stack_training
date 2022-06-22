from unicodedata import name
from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_id = models.CharField(primary_key='True',max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name