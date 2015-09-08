from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, UpdateView, \
    DeleteView
from .models import GpioR1, GpioR2
import RPi.GPIO as GPIO


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
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(4, GPIO.OUT)
        # GPIO.output(4, GPIO.HIGH)

    elif value == 'OFF':
        print("Light off")
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(4, GPIO.OUT)
        # GPIO.output(4, GPIO.LOW)


class GpioR2ConfListView(ListView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_list.html'

class GpioR2CreateView(CreateView):
    model = GpioR2
    fields = ('text', 'command', 'pin', 'param', )
    template_name = 'new_conf.html'

    def get_success_url(self):
        return reverse('conf_list')

class GpioR2DetailView(DetailView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_detail.html'

class GpioR2ConfEditView(UpdateView):
    model = GpioR2
    fields = ('text', 'command', 'pin', 'param', )
    template_name = 'conf_edit.html'

    def get_success_url(self):
        return reverse('conf_detail', args=(self.get_object().pk, ))

class GpioR2ConfDeleteView(DeleteView):
    model = GpioR2
    template_name = 'conf_confirm_delete.html'

    def get_success_url(self):
        return reverse('conf_list')
