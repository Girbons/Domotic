import os

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, \
    TemplateView

from domotic.forms import GpioR2Form

from .models import GpioR2


class GpioR2ConfListView(ListView):
    model = GpioR2
    queryset = GpioR2.objects.filter(action='toggle light')
    template_name = 'conf_list.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('light', None):
            pin = request.GET.get('pin')
            pk = request.GET.get('pk')
            light(pin, pk, request.GET.get('light'))
        return super(GpioR2ConfListView, self).get(request, *args, **kwargs)


class LockListView(ListView):
    model = GpioR2
    template_name = 'lock_list.html'
    queryset = GpioR2.objects.filter(action='lock')

    def get(self, request, *args, **kwargs):
        if request.GET.get('light', None):
            pin = request.GET.get('pin')
            pk = request.GET.get('pk')
            light(pin, pk, request.GET.get('light'))
        return super(LockListView, self).get(request, *args, **kwargs)


def light(pin, pk, value):
    is_raspberry = False
    if os.uname()[4].startswith("arm"):
        import RPi.GPIO as gpio
        is_raspberry = True

    if is_raspberry is True:
        s = GpioR2.objects.get(id=pk)
        if value == 'ON':
            s.status = 'ON'
            gpio.setmode(gpio.BCM)
            gpio.setup(int(pin), gpio.OUT)
            gpio.output(int(pin), gpio.HIGH)
        elif value == 'OFF':
            s.status = 'OFF'
            gpio.setmode(gpio.BCM)
            gpio.setup(int(pin), gpio.OUT)
            gpio.output(int(pin), gpio.LOW)
        s.save()


class GpioR2CreateView(CreateView):
    model = GpioR2
    form_class = GpioR2Form
    template_name = 'new_conf.html'

    def get_success_url(self):
        return reverse('settings')

    @method_decorator(permission_required('x.add_gpior2'))
    def dispatch(self, *args, **kwargs):
        return super(GpioR2CreateView, self).dispatch(*args, **kwargs)


class LightDetailView(DetailView):
    model = GpioR2
    queryset = GpioR2.objects.filter(action='toggle light')
    template_name = 'conf_detail.html'


class GpioR2ConfDeleteView(DeleteView):
    model = GpioR2
    template_name = 'conf_confirm_delete.html'

    def get_success_url(self):
        return reverse('light_settings')


class Profile(ListView):
    model = get_user_model()
    template_name = 'profile.html'


class PageNotFoundView(TemplateView):
    template_name = '404.html'


class HomepageView(TemplateView):
    template_name = 'homepage.html'


class SettingsView(TemplateView):
    template_name = 'settings.html'


class SettingsLightEditView(UpdateView):
    model = GpioR2
    fields = ('item', 'pin', )
    template_name = 'conf_edit.html'

    def get_success_url(self):
        return reverse('light_settings')


class LightSettingsListView(ListView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'light_settings_list.html'
