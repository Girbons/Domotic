from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.template.backends import django
from rest_framework import routers

from x import views
from .views import Profile


urlpatterns = [
    #homepage
    url(r'^$', login_required(views.HomepageView.as_view()), name='homepage'),
    #light configuration
    url(r'^light-control/$', login_required(views.GpioR2ConfListView.as_view()), name='conf_list'),
    #lock door configuration
    url(r'^lock-control/$', login_required(views.LockListView.as_view()), name='lock_list'),
    #temperature
    url(r'^temperature-control/$', login_required(views.TemperatureListView.as_view()), name='temp'),
    #new configuration
    url(r'^configuration/new/$', login_required(views.GpioR2CreateView.as_view()), name='new_conf'),
    url(r'^configuration/temperature/new/$', login_required(views.TemperatureCreate.as_view()), name='temp_new'),
    #broker new configuration
    url(r'^configuration-broker/new/$', login_required(views.BrokerCreate.as_view()), name='broker_new'),

    #url about user
    # url(r'^accounts/register/$', views.Registration.as_view(), name='register'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'logout.html'},
        name='logout'),
    url('^accounts/profile/$', login_required(Profile.as_view()), name='profile'),

    #page not found
    url(r'^404/$', views.PageNotFoundView.as_view(), name='404'),

    #settings urls
    url(r'^settings/$', login_required(views.SettingsView.as_view()), name='settings'),
    url(r'^settings/configuration-settings/$', login_required(views.LightSettingsListView.as_view()), name='light_settings'),
    url(r'^settings/temperature-settings/$', login_required(views.TemperatureSettingsListView.as_view()), name='temp_settings'),
    url(r'^settings/broker-settings/$', login_required(views.BrokerListView.as_view()), name='broker_list'),
    url(r'^settings/light/(?P<pk>[0-9]+)/edit/$', login_required(views.SettingsLightEditView.as_view()),
        name='conf_edit'),
    url(r'^settings/temperature/(?P<pk>[0-9]+)/edit/$', login_required(views.TemperatureEditConfiguration.as_view()),
        name='temp_edit'),
    url(r'^settings/broker/(?P<pk>[0-9]+)/edit/$', login_required(views.BrokerEditView.as_view()),
        name='broker_edit'),
    url(r'^configuration/(?P<pk>[0-9]+)/delete/$', login_required(views.GpioR2ConfDeleteView.as_view()),
        name='conf_delete'),
    url(r'^configuration/broker/(?P<pk>[0-9]+)/delete/$', login_required(views.BrokerDelete.as_view()),
        name='broker_delete'),
    url(r'^configuration/temperature/(?P<pk>[0-9]+)/delete/$', login_required(views.TemperatureDelete.as_view()),
        name='temp_delete'),
]

