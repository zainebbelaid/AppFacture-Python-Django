from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('home/', views.home, name='home'),
    path('login/', views.loginUser , name='login'),
    path('loginUser/', views.loginUser , name='loginUser'),
    path('register/', views.registerUser, name='register'),
    path('serviceclient', views.serviceclient, name ='serviceclient'),
    path('sendemaill',views.sendemaill,name='sendemaill'),
    path('logoutUser/', views.logoutUser , name='logoutUser'),   
]
