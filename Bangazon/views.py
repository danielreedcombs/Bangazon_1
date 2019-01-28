from django.shortcuts import render,  get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import *
# Create your views here.

def employees(request):
  employee_list = Employee.objects.all()
  context = {'employee_list': employee_list}
  return render(request, 'Bangazon/employees.html', context)


def departments(request):
  department_list = Department.objects.all()
  context = {'department_list': department_list}
  return render(request, 'Bangazon/departments.html', context)

def computers(request):
  computer_list = Computer.objects.all()
  context = {'computer_list': computer_list}
  return render(request, 'Bangazon/computers.html', context)

def training_programs(request):
  now = timezone.now()
  training_program_list = TrainingProgram.objects.filter(startDate__gte=now)
  context = {'training_program_list': training_program_list}
  return render(request, 'Bangazon/training_program.html', context)

def past_training_programs(request):
  now = timezone.now()
  training_program_list = TrainingProgram.objects.filter(startDate__lte=now)
  context = {'training_program_list': training_program_list}
  return render(request, 'Bangazon/past_training_programs.html', context)

def new_training_program_form(request):
  return render(request, 'Bangazon/new_training_program_form.html')

def save_program(request):
  name = request.POST['training_name']
  description = request.POST['training_description']
  startDate= request.POST['training_startDate']
  endDate = request.POST['training_endDate']
  maxEnrollment = request.POST['training_maxEnrollment']
  t = TrainingProgram(name = name, description = description, startDate = startDate, endDate = endDate, maxEnrollment = maxEnrollment)
  t.save()
  response = redirect('./Training')
  return response

def training_details(request, pk):
  training_program_details = get_object_or_404(TrainingProgram, id = pk)
  training_attendees = EmployeeTrainingProgram.objects.filter(trainingProgramId_id = pk)
  all_attendees = []
  for user in training_attendees:
    print(user.employeeId_id)
    employee_trained = get_object_or_404(Employee, id = user.employeeId_id)
    all_attendees.append(employee_trained)
  context = {'training_program_details': training_program_details, 'all_attendees': all_attendees}
  return render(request, 'Bangazon/indiv_training_program.html', context)