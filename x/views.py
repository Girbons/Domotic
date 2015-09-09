from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, UpdateView, \
    DeleteView, RedirectView, FormView
from .models import GpioR1, GpioR2



class ConfigurationRun(DetailView):
    model = GpioR2
    template_name = 'conf_run.html'
    queryset = GpioR2.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('light', None):
            pin = request.GET.get('pin')
            light(pin, request.GET.get('light'))
        return super(ConfigurationRun, self).get(request, *args, **kwargs)


def light(pin, value):
    if value == 'ON':
        import RPi.GPIO as GPIO
        print("Light on")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    elif value == 'OFF':
        print("Light off")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


class GpioR2ConfListView(ListView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_list.html'

class GpioR2CreateView(CreateView):
    model = GpioR2
    fields = ('text', 'pin', 'action', )
    template_name = 'new_conf.html'

    def get_success_url(self):
        return reverse('conf_list')


class GpioR2DetailView(DetailView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_detail.html'


class GpioR2ConfEditView(UpdateView):
    model = GpioR2
    fields = ('text', 'pin', 'action', )
    template_name = 'conf_edit.html'

    def get_success_url(self):
        return reverse('conf_detail', args=(self.get_object().pk, ))


class GpioR2ConfDeleteView(DeleteView):
    model = GpioR2
    template_name = 'conf_confirm_delete.html'

    def get_success_url(self):
        return reverse('conf_list')

