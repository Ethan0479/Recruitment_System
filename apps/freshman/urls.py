#coding=utf-8
from django.conf.urls import url
from django.urls import path

from .views import RegisterView, LoginView, PersonalView, IndexView


from . import views
urlpatterns = [
    # url(r'^login/$',views.login)
    # url(r'^register/$',views.)
    # url(r'^personal/$',views.)
    # url(r'^interview_time/$',views.)
    # url(r'^application/$',views.)
    # url(r'^result/$',views.)
    # url(r'^application/$',views.ApplicationView.get)
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('index/', IndexView.as_view(), name='index'),
    path('personal/', PersonalView.as_view(), name='personal')
]


