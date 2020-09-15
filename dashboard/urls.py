from django.urls import path,include
from . import views
urlpatterns = [
    path('startup_dashboard/',views.startup_dashboard,name='startup_dashboard'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_form/',views.admin_form,name='admin_form'),
]
