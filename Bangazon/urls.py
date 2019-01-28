from django.urls import path

from . import views

app_name = 'Bangazon'
urlpatterns = [
    path('Bangazon/Employees', views.employees, name='employees'),
    path('Bangazon/Departments', views.departments, name='departments'),

    path('Bangazon/Computers', views.computers, name='computers'),
    path('Bangazon/Computers/<int:computer_id>', views.computer_details, name='computer_details'),
    path('Bangazon/Computers/new', views.computer_new, name='computer_new'),
    path('Bangazon/Computers/form', views.computer_form, name='computer_form'),


    path('Bangazon/Training', views.training_programs, name='training_programs'),
    path('Bangazon/Training<int:pk>/', views.training_details, name='training_details'),
    path('Bangazon/PastTraining', views.past_training_programs, name='past_training_programs'),
]