from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, \
    TemplateView
from .models import GpioR1, GpioR2


class GpioR2ConfListView(ListView):
    model = GpioR2
    queryset = GpioR2.objects.all()
    template_name = 'conf_list.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('light', None):
            pin = request.GET.get('pin')
            pk = request.GET.get('pk')
            light(pin, pk, request.GET.get('light'))
        elif request.GET.get('get_temp'):
            pin = request.GET.get('pin')
            sensor = request.GET.get('dht')
            get_temp(pin, sensor)
        return super(GpioR2ConfListView, self).get(request, *args, **kwargs)


def get_temp(pin, sensor):
    import sys
    import Adafruit_Python_DHT.Adafruit_DHT as Adafruit_DHT

    # Parse command line parameters.
    # sensor_args = {'11': Adafruit_DHT.DHT11,
    #                '22': Adafruit_DHT.DHT22,
    #                '2302': Adafruit_DHT.AM2302}
    # if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    #     sensor = sensor_args[sys.argv[1]]
    #     pin = sys.argv[2]
    # else:
    #     print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    #     print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    #     sys.exit(1)

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(int(sensor), int(pin))

    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
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

