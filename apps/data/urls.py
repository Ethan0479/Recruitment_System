from django.conf.urls import url
from django.urls import path

from . import views
urlpatterns = [
    url(r'^data/bar1/$', views.bar1),
    url(r'^data/bar2/$', views.bar2),
    url(r'^data/bar3/$', views.bar3),
    path('manage/', views.manage),
]