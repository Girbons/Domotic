from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, \
    TemplateView
# from .forms import RegistrationForm
from .models import GpioR1, GpioR2, Temperature


class GpioR2ConfListView(ListView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_list.html'

    def get_context_data(self, **kwargs):
        context = super(GpioR2ConfListView, self).get_context_data(**kwargs)
        context.update({'temp': Temperature.objects.get(id=1)})
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('light', None):
            pin = request.GET.get('pin')
            pk = request.GET.get('pk')
            light(pin, pk, request.GET.get('light'))
        elif request.GET.get('get_temp'):
            pin = request.GET.get('pin')
            sensor = request.GET.get('dht')
            pk = request.GET.get('pk')
            get_temp(pin, sensor, pk)
        return super(GpioR2ConfListView, self).get(request, *args, **kwargs)


def get_temp(pin, sensor, pk):
    import sys
    import Adafruit_DHT

    termos = Temperature.objects.get(id=1)
    humidity, temperature = Adafruit_DHT.read_retry(int(sensor), int(pin))
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        termos.temperature = temperature
        termos.Humidity = humidity
        termos.save()
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)


def light(pin, pk, value):
    s = GpioR2.objects.get(id=pk)
    import RPi.GPIO as gpio
    if value == 'ON':
        s.status = 'ON'
        print("Light on")
        gpio.setmode(gpio.BCM)
        gpio.setup(int(pin), gpio.OUT)
        gpio.output(int(pin), gpio.HIGH)
    elif value == 'OFF':
        print("Light off")
        s.status = 'OFF'
        gpio.setmode(gpio.BCM)
        gpio.setup(int(pin), gpio.OUT)
        gpio.output(int(pin), gpio.LOW)
    s.save()


class GpioR2CreateView(CreateView):
    model = GpioR2
    fields = ('text', 'pin', 'action', 'image', )
    template_name = 'new_conf.html'

    def get_success_url(self):
        return reverse('conf_list')

    @method_decorator(permission_required('x.add_gpior2'))
    def dispatch(self, *args, **kwargs):
        return super(GpioR2CreateView, self).dispatch(*args, **kwargs)


class GpioR2DetailView(DetailView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_detail.html'


class GpioR2ConfEditView(UpdateView):
    model = GpioR2
    fields = ('text', 'pin', 'action', 'image', )
    template_name = 'conf_edit.html'

    def get_success_url(self):
        return reverse('conf_detail', args=(self.get_object().pk, ))

    @method_decorator(permission_required('x.change_gpior2'))
    def dispatch(self, *args, **kwargs):
        return super(GpioR2ConfEditView, self).dispatch(*args, **kwargs)


class GpioR2ConfDeleteView(DeleteView):
    model = GpioR2
    template_name = 'conf_confirm_delete.html'

    def get_success_url(self):
        return reverse('conf_list')

    @method_decorator(permission_required('x.delete_gpior2'))
    def dispatch(self, request, *args, **kwargs):
        return super(GpioR2ConfDeleteView, self).dispatch(request, *args, **kwargs)


class Profile(ListView):
    model = get_user_model()
    template_name = 'profile.html'


class PageNotFoundView(TemplateView):
    template_name = '404.html'


class GpioR1CreateView(CreateView):
    model = GpioR1
    fields = ('text', 'pin', 'action', )
    template_name = 'new_conf.html'

    def get_success_url(self):
        return reverse('conf_list')


class TemperatureListView(ListView):
    model = Temperature
    queryset = Temperature.objects.all()
    template_name = 'prova.html'



# class Registration(CreateView):
#      model = get_user_model()
#      template_name = 'register.html'
#      form_class = RegistrationForm
#      def get_success_url(self):
#         return reverse('login')

