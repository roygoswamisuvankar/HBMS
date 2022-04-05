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
]