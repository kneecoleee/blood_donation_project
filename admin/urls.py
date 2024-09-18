# admin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('manage_donors/', views.manage_donors_view, name='manage_donors'),
    path('manage_recipients/', views.manage_recipients_view, name='manage_recipients'),
]