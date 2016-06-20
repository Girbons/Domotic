from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, \
    TemplateView
# from .forms import RegistrationForm
from x.forms import GpioR2Form
from .models import GpioR2, Temperature, MqttBroker


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

class TemperatureListView(ListView):
    model = Temperature
    queryset = Temperature.objects.all()
    template_name = 'temperature.html'


def light(pin, pk, value):
    check = False

    try:
        import RPi.GPIO as gpio
        check = True
    except ImportError:
        print 'cannot import rpi.gpio library'

    if check is True:
        s = GpioR2.objects.get(id = pk)
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
        return reverse('settings')

    @method_decorator(permission_required('x.delete_gpior2'))
    def dispatch(self, request, *args, **kwargs):
        return super(GpioR2ConfDeleteView, self).dispatch(request, *args, **kwargs)


class Profile(ListView):
    model = get_user_model()
    template_name = 'profile.html'


class PageNotFoundView(TemplateView):
    template_name = '404.html'


class HomepageView(TemplateView):
    template_name = 'homepage.html'


class SettingsView(TemplateView):
    template_name = 'settings.html'



#TODO view for delete and edit the configuration
# class SettingsEditView(ListView):
#     model = GpioR2

# class Registration(CreateView):
#      model = get_user_model()
#      template_name = 'register.html'
#      form_class = RegistrationForm
#      def get_success_url(self):
#         return reverse('login')

