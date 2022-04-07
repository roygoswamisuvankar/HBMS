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
]