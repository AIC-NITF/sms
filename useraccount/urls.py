from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('admin_register',views.admin_register,name='admin_register'),
    path('startup_register',views.startup_register,name='startup_register'),
]