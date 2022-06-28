from django.contrib import admin
from .models import Process_data, Cnn_model,auth_user
# Register your models here.
admin.site.register(Process_data)
admin.site.register(Cnn_model)
admin.site.register(auth_user)