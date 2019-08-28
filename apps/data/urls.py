from django.conf.urls import url
from django.urls import path

from . import views
urlpatterns = [
    url(r'^bar1/$', views.bar1),
    url(r'^bar2/$', views.bar2),
    url(r'^data/bar3/$', views.bar3),
    path('manage/', views.manage),
    path('manage/timedata/', views.timedata),
    path('manage/test/', views.appoint_interview_time),
    path('manage/<slug:num>/', views.creatimg)
]