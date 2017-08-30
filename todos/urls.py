from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task, name='task'),
    # /(?P<id>\w{0,50})/ this is the id of the current cursor
    url(r'^todos/details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^todos/add$', views.add, name='add'),

]
