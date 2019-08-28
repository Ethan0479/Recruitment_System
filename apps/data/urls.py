from django.conf.urls import url
from django.urls import path

from . import views
urlpatterns = [
    path('manage/', views.manage),
    path('manage/timedata/', views.timedata),
    path('manage/test/', views.appoint_interview_time),
    path('manage/<slug:num>/', views.creatimg)
]