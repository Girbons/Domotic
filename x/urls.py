from django.conf.urls import include, url
from x import views

urlpatterns = [
    url(r'^$', views.Dio.as_view(), name='home'),
]
