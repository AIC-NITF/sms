from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('admin_form/',views.admin_form,name='admin_form'),
    path('startup_form/',views.startup_form,name='startup_form'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('profile/<int:pk>/edit_startup/',views.startup_profile_edit,name='startup_profile_edit'),
    #path('profile/<int:pk>/edit_employee/',views.employee_profile_edit,name='employee_profile_edit'),
    #path('profile/<int:pk>/delete_employee/',views.delete_employee,name='delete_employee'),
    path('edit_emp_form',views.edit_emp_form,name='edit_emp_form'),
    path('profile/delete_employee/',views.delete_employee,name='delete_employee'),
    path('edit_emp_form',views.edit_emp_form,name='edit_emp_form'),
    path('userprofile/<int:pk>/',views.userprofile,name='userprofile'),
    path('add_new_team_member',views.add_new_team_member,name='add_new_team_member'),
    
    path('delete_team_member',views.delete_team_member,name='delete_team_member'),
    path('edit_team_member',views.edit_team_member,name='edit_team_member'),

    path('monitor_sheet/',views.monitor_sheet,name='monitor_sheet'),
    path('traction_sheet/',views.traction_sheet,name='traction_sheet'),
    path('minute_of_meeting/',views.minute_of_meeting,name='minute_of_meeting'),

    path('monitor_form/',views.monitor_form,name='monitor_form'),
    path('monitor_report/<int:pk>/',views.monitor_report,name='monitor_report'),
    
    path('allowedit/<int:pk>',views.allowedit,name='allowedit'),
    path('monitor_sheet_edit/<int:pk>',views.monitor_sheet_edit,name='monitor_sheet_edit'),
]
