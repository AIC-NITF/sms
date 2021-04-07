from django.urls import path
from . import views

urlpatterns = [
    path('', views.sanvriddhi,name='sanvriddhi'),
    path('sanvriddhi_form', views.sanvriddhi_form,name='iframe'),
]
