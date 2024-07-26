from django.urls import path
from . import views

app_name = 'ResumePage'

urlpatterns = [
    path('', views.home, name='home'),
    path('resume_list/', views.resume_list, name='resume_list'),
    path('resume_detail/<int:pk>/', views.resume_detail, name='resume_detail'),

    path('resume_delete/<int:pk>/', views.resume_delete, name='resume_delete'),
    path('resume_new/', views.resume_new, name='resume_new'),
]