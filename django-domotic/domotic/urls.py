from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from domotic import views

from .views import Profile


urlpatterns = [
    # homepage
    url(r'^$', login_required(views.HomepageView.as_view()), name='homepage'),
    # light configuration
    url(r'^light-control/$', login_required(views.GpioR2ConfListView.as_view()), name='conf_list'),
    # new configuration
    url(r'^configuration/new/$', views.GpioR2CreateView.as_view(), name='new_conf'),

    # url about user
    # url(r'^accounts/register/$', views.Registration.as_view(), name='register'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'logout.html'},
        name='logout'),
    url('^accounts/profile/$', login_required(Profile.as_view()), name='profile'),

    # page not found
    url(r'^404/$', views.PageNotFoundView.as_view(), name='404'),

    # settings urls
    url(r'^settings/$', login_required(views.SettingsView.as_view()), name='settings'),
    url(r'^settings/configuration-settings/$', login_required(views.LightSettingsListView.as_view()),
        name='light_settings'),
    url(r'^settings/light/(?P<pk>[0-9]+)/edit/$', login_required(views.SettingsLightEditView.as_view()),
        name='conf_edit'),
    url(r'^configuration/(?P<pk>[0-9]+)/delete/$', login_required(views.GpioR2ConfDeleteView.as_view()),
        name='conf_delete'),
]
