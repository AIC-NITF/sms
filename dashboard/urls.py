from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('admin_form/',views.admin_form,name='admin_form'),
    path('startup_form/',views.startup_form,name='startup_form'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('profile/<int:pk>/edit/',views.profile_edit,name='profile_edit'),
]
