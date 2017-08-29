from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task, name='task'),
    # /(?P<id>\w{0,50})/ this is the id of the current cursor
    url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details'),
    url(r'^add', views.add, name='add'),

]
