from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ads/$', views.ads, name='ads'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^mydevices/$', views.DevicesByUserView, name='my-devices'),
    url(r'^newdevice/$', views.NewDevice, name='new-device'),
    url(r'^delete/(?P<id>\d+)/$', views.delete),
]