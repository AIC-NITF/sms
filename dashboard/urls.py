from django.urls import path,include
# from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve
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

    path('traction_form/',views.traction_form,name='traction_form'),
    path('traction_report/<int:pk>/',views.traction_report,name='traction_report'),
    path('allow_traction_edit/<int:pk>',views.allow_traction_edit,name='allow_traction_edit'),
    path('edit_traction_sheet/<int:pk>',views.edit_traction_sheet,name='edit_traction_sheet'),




    path('visit_startup/',views.visit_startup,name='visit_startup'),
    path('generate_work/',views.generate_work,name='generate_work'),
    path('edit_work/',views.edit_work,name='edit_work'),
    path('visit_employee/<int:pk>/',views.visit_employee,name='visit_employee'),

    path('start/<int:pk>/',views.start,name='start'),
    path('completed/<int:pk>/',views.completed,name='completed'),

    path('forward_work/',views.forward_work,name='forward_work'),
    path('return_work/',views.return_work,name='return_work'),
    path('reassign/',views.reassign,name='reassign'),
    path('return_start/<int:pk>/',views.return_start,name='return_start'),

    path('delete_work/<int:pk>',views.delete_work,name='delete_work'),
    #url(r'^download/(?P<path>.*)$', serve, {'document root': settings.MEDIA_ROOT}),
]
