from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('logout1',views.logout1,name='logout1'),
    path('admin_register',views.admin_register,name='admin_register'),
    path('startup_register',views.startup_register,name='startup_register'),

    path('sanvriddhi_register',views.sanvriddhi_register,name='sanvriddhi_register'),
]