from django import forms
from django.forms import fields
from .models import GpioR1, GpioR2

class GpioR1Form(forms.ModelForm):
    class Meta:
        model = GpioR1
        fields = ('command', 'param', 'pin',)

class GpioR2Form(forms.ModelForm):
    class Meta:
        model = GpioR2
        fields = ('text', 'pin', 'param', 'command',)
