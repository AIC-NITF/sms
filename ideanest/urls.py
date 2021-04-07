from django.urls import path
from . import views

urlpatterns = [
    path('', views.ideanest,name='ideanest'),
    path('ideanest_form', views.ideanest_form,name='ideanest_form_iframe'),
]
