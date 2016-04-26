from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import GpioR1, GpioR2, Temperature, Icon

# Register your models here.
admin.site.register(GpioR1)
admin.site.register(Permission)
admin.site.register(GpioR2)
admin.site.register(Temperature)
admin.site.register(Icon)
