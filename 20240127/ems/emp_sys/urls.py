from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('company', views.all_comp, name='all_comp'),
    path('employee', views.all_emp, name='all_emp'),
    path('company/<int:id>', views.comp, name='comp'),
    path('company/<int:id>/delete', views.del_comp, name='del_comp'),
    path('employee/<int:id>/delete', views.del_emp, name='del_emp'),
    path('employee/add' , views.add_emp, name='add_emp'),
    path('company/add' , views.add_comp, name='add_comp')

    
]
