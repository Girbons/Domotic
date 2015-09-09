from django.conf.urls import include, url
from x import views

urlpatterns = [
    url(r'^$', views.GpioR2ConfListView.as_view(), name='conf_list'),
    url(r'^configuration/new/$', views.GpioR2CreateView.as_view(), name='new_conf'),
    url(r'^configuration/(?P<pk>[0-9]+)/detail/$', views.GpioR2DetailView.as_view(),
        name='conf_detail'),
    url(r'^configuration/(?P<pk>[0-9]+)/edit/$', views.GpioR2ConfEditView.as_view(),
        name='conf_edit'),
    url(r'^configuration/(?P<pk>[0-9]+)/delete/$', views.GpioR2ConfDeleteView.as_view(),
        name='conf_delete'),
    url(r'^configuration/(?P<pk>[0-9]+)/run/$', views.ConfigurationRun.as_view(),
        name='conf_run'),
]
