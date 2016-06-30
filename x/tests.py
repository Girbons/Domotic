from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import GpioR2


class TestViews(TestCase):
    def setUp(self):
        User.objects.create_user('dio', password='123456', email='a@a.it')
        self.conf = GpioR2.objects.create(text="dio", pin="2", action="toggle light")

    def test_conf_list_return_200_after_login(self):
        self.client.login(username='dio', password='123456')
        response = self.client.get(reverse('conf_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.conf.pin)

    def test_new_conf_without_login(self):
        response = self.client.get(reverse('new_conf'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/accounts/login/?next=/configuration/new/')

    def test_new_conf_with_login_with_perm(self):
        user = self.client.login(username='dio', password='123456')
        data = {'text': 'test', 'pin': '4', 'action': 'toggle light'}
        response = self.client.get(reverse('new_conf'), data=data)
        self.assertEqual(response.status_code, 200)

    def test_conf_edit_with_login(self):
        user = self.client.login(username='dio', password='123456')
        data = {'text': 'siao', 'pin': '4', 'action': 'toggle light'}
        response = self.client.post(reverse('conf_edit', args=(self.conf.pk, )),  data=data)
        self.assertEqual(response.status_code, 302)
        conf = GpioR2.objects.get(pk=self.conf.pk)
        self.assertEqual(conf.pin, 4)

    def test_conf_edit_without_login(self):
        response = self.client.post(reverse('conf_edit', args=(self.conf.pk, )))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/accounts/login/?next=/configuration/1/edit/')

    def test_conf_detail_return_200(self):
        response = self.client.get(reverse('conf_detail', args=(self.conf.pk, )))
        self.assertEqual(response.status_code, 200)

    def test_profile_return_200_after_login(self):
        self.client.login(username='dio', password='123456')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)


