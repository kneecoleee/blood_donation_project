# blood_donation_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('blood/', include('blood.urls')),
    path('admin/', include('admin.urls')),
]