from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, \
    TemplateView

from x.serializers import GpioR1Serializer, GpioR2Serializer
from .models import GpioR1, GpioR2
from rest_framework import viewsets


class GpioR2ConfListView(ListView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_list.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('light', None):
            pin = request.GET.get('pin')
            light(pin, request.GET.get('light'))
        return super(GpioR2ConfListView, self).get(request, *args, **kwargs)


def light(pin, value):
    import RPi.GPIO as gpio
    if value == 'ON':
        print("Light on")
        gpio.setmode(gpio.BCM)
        gpio.setup(int(pin), gpio.OUT)
        gpio.output(int(pin), gpio.HIGH)

    elif value == 'OFF':
        print("Light off")
        gpio.setmode(gpio.BCM)
        gpio.setup(int(pin), gpio.OUT)
        gpio.output(int(pin), gpio.LOW)


class GpioR2CreateView(CreateView):
    model = GpioR2
    fields = ('text', 'pin', 'action', )
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
    fields = ('text', 'pin', 'action', )
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

