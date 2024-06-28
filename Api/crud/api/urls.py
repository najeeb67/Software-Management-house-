from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.add_employee, name='add_employee'),
    path('employee/<int:employee_id>/' , views.get_employee_data , name="get_employee_data"),
    path('employee/update/<int:employee_id>' , views.update_employe, name="update_employe"),
    path('employee/delete/<int:employee_id>', views.delete_employe, name="delete_employee")
]
