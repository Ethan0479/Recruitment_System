#coding=utf-8
from django.conf.urls import url
from django.urls import path


from .views import IndexView, LoginView, RegisterView, PersonalView, InterviewResultView, HomepageView, AppointmentView

app_name = 'freshman'
urlpatterns = [
    # url(r'^login/$',views.login)
    # url(r'^register/$',views.)
    # url(r'^personal/$',views.)
    # url(r'^interview_time/$',views.)
    # url(r'^application/$',views.)
    # url(r'^result/$',views.)
    # url(r'^application/$',views.ApplicationView.get)
    url('index/', IndexView.as_view(), name='index'),
    url('login/', LoginView.as_view(), name='login'),
    url('register/', RegisterView.as_view(), name='register'),
    url('alterinfo/', PersonalView.as_view(), name='alterinfo'),
    url('result/', InterviewResultView.as_view(), name='result'),
    url('homepage/', HomepageView.as_view(), name='homepage'),
    url('sign_up/', AppointmentView.as_view(), name='sign_up'),
]


