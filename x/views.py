from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View, TemplateView


class Dio(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('light', None):
            toggle_light(request.GET.get('light'))
        return super(Dio, self).get(request, *args, **kwargs)



def toggle_light(value):
    if value == 'ON':
        # Comandi per accendere la luce
        print("Light on")
    elif value == 'OFF':
        print("Light off")
