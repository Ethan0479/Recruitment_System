#coding=utf-8
from django.conf.urls import url
from django.urls import path

from . import views
from .views import *

app_name = 'freshman'




urlpatterns = [
    # url(r'^login/$',views.login)
    # url(r'^register/$',views.)
    # url(r'^personal/$',views.)
    # url(r'^interview_time/$',views.)
    # url(r'^application/$',views.)
    # url(r'^result/$',views.)
    # url(r'^application/$',views.ApplicationView.get)
    url(r'^$', ensure_csrf_cookie(IndexView.as_view()), name='index'),
    url(r'^index/$', ensure_csrf_cookie(IndexView.as_view()), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', ensure_csrf_cookie(RegisterView.as_view()), name='register'),
    url(r'^alterinfo/$', PersonalView.as_view(), name='alterinfo'),
    url(r'^result/$', InterviewResultView.as_view(), name='result'),
    url(r'^homepage/$', HomepageView.as_view(), name='homepage'),
    url(r'^sign_up/$', AppointmentView.as_view(), name='sign_up'),
    url(r'^alter_sign_up/$', AlterAppointmentView.as_view(), name='alter_sign_up'),
    url(r'^application/$', ApplicationView.as_view(), name='application'),
    url(r'^get_major/$', get_major, name='get_major'),
    url(r'^email_code', send_code_by_email, name='email_code'),
]

