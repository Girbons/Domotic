from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth.models import User
from .models import GpioR1, GpioR2, Temperature


class GpioR1Form(forms.ModelForm):
    class Meta:
        model = GpioR1
        fields = ('text', 'pin', 'action', )


class GpioR2Form(forms.ModelForm):
    class Meta:
        model = GpioR2
        fields = ('text', 'pin', 'action', 'image', )


class SensorForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = ('pin', 'sensor', )

# class RegistrationForm(UserCreationForm):
#     email = fields.EmailField()
#     first_name = fields.CharField(max_length=50)
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'username', 'email', 'password1', 'password2', )
#
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         first_name = self.cleaned_data['first_name']
#         user.first_name = first_name
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
