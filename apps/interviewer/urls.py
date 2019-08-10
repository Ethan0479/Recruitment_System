#coding=utf-8
from django.urls import path
from .views import RegisterView, LoginView, Audition

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('index/', Audition.as_view(), name='audition'),
]