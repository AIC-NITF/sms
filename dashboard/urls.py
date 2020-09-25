from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('admin_form/',views.admin_form,name='admin_form'),
    path('startup_form/',views.startup_form,name='startup_form'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('profile/<int:pk>/edit_startup/',views.startup_profile_edit,name='startup_profile_edit'),
    path('profile/<int:pk>/edit_employee/',views.employee_profile_edit,name='employee_profile_edit'),
    # path('profile/<int:pk>/delete_employee/',views.delete_employee,name='delete_employee'),
    path('edit_emp_form',views.edit_emp_form,name='edit_emp_form'),
]
