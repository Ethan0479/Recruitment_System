#coding=utf-8
from django.urls import path
from . import views
from .views import RegisterView, LoginView, Audition

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('management/', Audition.as_view(), name='management'),
    path('management/inter_search_son/', views.internal),
    path('search/', views.freshman_search),
]