from django.test import TestCase

from ..models import GpioR2 as gpior2


class TestGpioR2(TestCase):

    def test_configuration_create(self):
        gpior2.objects.create(item='item test', pin=2, action='toggle light',
                              status='Undefined')
        self.assertEqual(gpior2.objects.count(), 1)

    def test_configuration_params(self):
        conf = gpior2.objects.create(item='light test', pin=2, action='toggle_light',
                                     status='Undefined')
        self.assertEqual(conf.item, 'light test')
        self.assertEqual(conf.pin, 2)
        self.assertEqual(conf.action, 'toggle_light')
        self.assertEqual(conf.status, 'Undefined')

    def test_configuration(self):
        configuration = gpior2.objects.create(item='item test', pin=2, action='toggle light',
                                              status='Undefined')
        self.assertEqual(configuration.item, 'item test')
        self.assertEqual(str(configuration), configuration.item)
