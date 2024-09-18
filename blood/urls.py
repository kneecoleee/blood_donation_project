# blood/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('donor_list/', views.donor_list_view, name='donor_list'),
    path('recipient_list/', views.recipient_list_view, name='recipient_list'),
]