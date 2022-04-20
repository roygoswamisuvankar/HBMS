from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    #home page index.html path
    path('', views.index, name='index'),

    #admin login page -> admin.html
    path('admin', views.admin, name='admin'),

    #admin login function goto admin home page
    path('adminlogin', views.adminlogin, name='adminlogin'),
    #admin home
    path('admin_home', views.admin_home, name='admin_home'),
    #admin logout
    path('adminlogout', views.adminlogout, name='adminlogout'),
    #admin -> add employees goto addemployees functions
    path('addemployees', views.addemployees, name='addemployees'),
    #admin-> show employees,
    path('show_emp', views.show_emp, name='show_emp'),
    #admin -> employee delete,
    path('emp_delete/<int:id>', views.emp_delete, name='emp_delete'),
    #admin-> edit employees
    path('emp_edit/<int:id>', views.emp_edit, name='emp_edit'),
    #admin -> update employee records, 
    path('emp_edit/update_emp', views.update_emp, name='update_emp'),
    #----------------------Employee sections---------------------------------------------
    #employee login path,
    path('employeelogin', views.employeelogin, name='employeelogin'),
    #employee login function
    path('employee_login', views.employee_login, name='employee_login'),
    path('employee_home', views.employee_home, name='employee_home'),
    #logout path
    path('emplogout', views.emplogout, name='emplogout'),
    #add rooms function
    path('addrooms', views.addrooms, name='addrooms'),
    #save data to database,
    path('addrooms1', views.addrooms1, name='addrooms1'),
    #checkin.html page,
    path('check_in', views.check_in, name='check_in'),
    #show available rooms date wise,
    path('show_av', views.show_av, name='show_av'),
    #book rooms,
    path('roombooked/<int:id>', views.roombooked, name='roombooked'),
    #room_booked,
    path('roombooked/booked_room', views.booked_room, name='booked_room'),
]