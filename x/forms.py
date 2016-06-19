from django import forms
from .models import GpioR2, Temperature


class GpioR2Form(forms.ModelForm):
    class Meta:
        model = GpioR2
        fields = ('room', 'item', 'pin', 'action', )


class SensorForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = ('room', 'data', )

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
