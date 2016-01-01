from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.template.backends import django
from rest_framework import routers

from x import views
from .views import Profile


urlpatterns = [
    url(r'^$', login_required(views.GpioR2ConfListView.as_view()), name='conf_list'),
    url(r'^configuration/new/$', login_required(views.GpioR2CreateView.as_view()), name='new_conf'),
    url(r'^configuration/(?P<pk>[0-9]+)/detail/$', login_required(views.GpioR2DetailView.as_view()),
        name='conf_detail'),
    url(r'^configuration/(?P<pk>[0-9]+)/edit/$', login_required(views.GpioR2ConfEditView.as_view()),
        name='conf_edit'),
    url(r'^configuration/(?P<pk>[0-9]+)/delete/$', login_required(views.GpioR2ConfDeleteView.as_view()),
        name='conf_delete'),
    # url(r'^accounts/register/$', views.Registration.as_view(), name='register'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'logout.html'},
        name='logout'),
    url('^accounts/profile/$', login_required(Profile.as_view()), name='profile'),
    url(r'^404/$', views.PageNotFoundView.as_view(), name='404'),


]
