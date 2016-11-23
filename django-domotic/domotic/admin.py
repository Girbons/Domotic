from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import GpioR2, Temperature, MqttBroker

# Register your models here.
admin.site.register(Permission)
admin.site.register(GpioR2)
admin.site.register(Temperature)
admin.site.register(MqttBroker)
