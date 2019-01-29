from django.urls import path
from . import views

app_name = 'Bangazon'
urlpatterns = [
    path('Bangazon/Employees', views.employees, name='employees'),
    path('Bangazon/Employees/<int:employee_id>', views.employee_details, name='employee_details'),


    path('Bangazon/Departments/', views.departments, name='departments'),
    path('Bangazon/Departments/NewDepartment', views.new_department, name='new_department'),
    path('Bangazon/Departments/SaveDepartment', views.save_department, name='save_department'),
    path('Bangazon/Departments/<int:department_id>', views.department_details, name='department_details'),


    path('Bangazon/Computers', views.computers, name='computers'),
    path('Bangazon/Computers/<int:computer_id>', views.computer_details, name='computer_details'),
    path('Bangazon/Computers/new', views.computer_new, name='computer_new'),
    path('Bangazon/Computers/form', views.computer_form, name='computer_form'),


    path('Bangazon/Training', views.training_programs, name='training_programs'),
    path('Bangazon/Training<int:pk>/', views.training_details, name='training_details'),
    path('Bangazon/PastTraining', views.past_training_programs, name='past_training_programs'),
    path('Bangazon/NewTrainingClass', views.new_training_program_form, name='new_training_program_form'),
    path('Bangazon/SaveProgram', views.save_program, name='save_program'),
]

