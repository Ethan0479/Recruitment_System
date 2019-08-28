#coding=utf-8
from django.urls import path
from . import views
from .views import RegisterView, LoginView, Audition, Inter_addfreshman

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('management/', Audition.as_view(), name='management'),
    path('management/inter_search_son/', views.freshman_search),
    path('search/', views.freshman_search),
    path('interviewed/', views.interviewed),
    path('inter_addfreshman/', Inter_addfreshman.as_view(), name='addfreshman'),
    path('logout/', views.acc_logout),
    path('management/<slug:a>/', views.info_check_out),
]