from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.login,name='login'),
    path('login/login', views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/add_appointment', views.add_appointment,name='add_appointment'),
    path('dashboard/add_prescription', views.add_prescription,name='add_prescription'),
    path('dashboard/add_patient', views.add_patient,name='add_patient'),
    path('dashboard/dashboard', views.dashboard,name='dashboard'),

]