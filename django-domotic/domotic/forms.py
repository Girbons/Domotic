from django import forms
from .models import GpioR2, Temperature


class GpioR2Form(forms.ModelForm):
    class Meta:
        model = GpioR2
        fields = ('item', 'pin', 'action', )


class SensorForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = ('data', )
