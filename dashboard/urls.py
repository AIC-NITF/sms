from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('admin_form/',views.admin_form,name='admin_form'),
    path('startup_form/',views.startup_form,name='startup_form'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('profile/<int:pk>/edit_startup/',views.startup_profile_edit,name='startup_profile_edit'),
    path('profile/delete_employee/',views.delete_employee,name='delete_employee'),
    path('edit_emp_form',views.edit_emp_form,name='edit_emp_form'),
    path('userprofile/<int:pk>/',views.userprofile,name='userprofile'),
    path('add_new_team_member',views.add_new_team_member,name='add_new_team_member'),
    
    path('delete_team_member',views.delete_team_member,name='delete_team_member'),
    path('edit_team_member',views.edit_team_member,name='edit_team_member'),
]
