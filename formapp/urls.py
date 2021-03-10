from django.urls import path
from . import views

urlpatterns = [
    path('', views.anantya,name='ocf_anantya'),
    path('entrepreneur_form/', views.entrepreneur_form,name='entrepreneur_form'),
    path('startup_form_app/', views.startup_form_app,name='startup_form_app'),
    path('entrepreneurform/', views.entrepreneurform,name='entrepreneurform'),
    path('startupform/', views.startupform,name='startupform'),
    path('details/', views.details,name='details'),
    path('eligibility/', views.eligibility,name='eligibility'),
]
