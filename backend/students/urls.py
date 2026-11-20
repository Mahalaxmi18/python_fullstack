
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.student_logout, name='logout'),
]
