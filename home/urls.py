from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('query_message/', views.query_message,name='query_message'),
    path('SWEA/', views.SWEA,name='SWEA'),
]
