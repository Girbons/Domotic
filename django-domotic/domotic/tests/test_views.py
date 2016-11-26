from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse

from ..models import GpioR2 as gpior2


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        get_user_model().objects.create_user(username='username', password='123456',
                                             email='test@test.it')
        self.conf = gpior2.objects.create(item='test', pin=2, action='toggle light',
                                          status='undefined')
        self.factory = RequestFactory()

    def test_homepage_view_without_login(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 302)

    def test_homepage_view(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_configuration_list_without_login(self):
        response = self.client.get(reverse('conf_list'))
        self.assertEqual(response.status_code, 302)

    def test_configuration_list(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('conf_list'))
        self.assertEqual(response.status_code, 200)

    def test_new_configuration_without_login(self):
        response = self.client.get(reverse('new_conf'))
        self.assertEqual(response.status_code, 302)

    def test_settings_view_without_login(self):
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 302)

    def test_settings_view(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)

    def test_404_view(self):
        response = self.client.get(reverse('404'))
        self.assertEqual(response.status_code, 200)

    def test_conf_list_view_without_login(self):
        response = self.client.get(reverse('conf_list'))
        self.assertEqual(response.status_code, 302)

    def test_conf_list_view(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('conf_list'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_without_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_light_settings_view_without_login(self):
        response = self.client.get(reverse('light_settings'))
        self.assertEqual(response.status_code, 302)

    def test_light_settings_view(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('light_settings'))
        self.assertEqual(response.status_code, 200)

    def test_new_conf_view(self):
        """
        This test should return 200 instead of 302
        """
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('new_conf'))
        self.assertEqual(response.status_code, 302)

    def test_conf_edit(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('conf_edit', args=(self.conf.pk, )))
        self.assertEqual(response.status_code, 200)

    def test_delete_config(self):
        self.client.login(username='username', password='123456')
        response = self.client.get(reverse('conf_delete', args=(self.conf.pk, )))
        self.assertEqual(response.status_code, 200)

    def test_conf_edit_without_login(self):
        response = self.client.get(reverse('conf_edit', args=(self.conf.pk, )))
        self.assertEqual(response.status_code, 302)
