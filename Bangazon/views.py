from django.shortcuts import render,  get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .forms import *
from .models import *
import datetime
import pytz





# ======================== EMPLOYEES ================
def employees(request):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'Bangazon/employees.html', context)


def employee_details(request, employee_id):
    now = timezone.now()
    employee_details = Employee.objects.get(pk=employee_id)
    past_training_programs = list()
    upcoming_training_programs = list()
    for program in employee_details.trainingprogram_set.all():
        if (program.startDate < now):
            past_training_programs.append(program)
        elif (program.startDate > now):
            upcoming_training_programs.append(program)
    context = {
        'employee_details': employee_details,
        'past_training_programs': past_training_programs,
        'upcoming_training_programs': upcoming_training_programs
    }
    return render(request, 'Bangazon/employee_details.html', context)

def employee_form(request):
    departments = Department.objects.all()
    context = {"departments": departments}
    return render(request, "Bangazon/employees_form.html", context)

def employee_new(request):
    department = Department.objects.get(pk=request.POST['department'])
    employee = Employee(firstName = request.POST['firstName'], lastName = request.POST['lastName'], startDate = request.POST['startDate'], isSupervisor = request.POST['supervisor'], department = department)

    employee.save()
    return HttpResponseRedirect(reverse('Bangazon:employees'))

# ========================DEPARTMENTS================


def departments(request):
    department_list = Department.objects.all()
    context = {'department_list': department_list}
    return render(request, 'Bangazon/departments.html', context)


def new_department(request):
    department_list = Department.objects.all()
    context = {'department_list': department_list}
    return render(request, 'Bangazon/new_department_form.html', context)


def save_department(request):
    name = request.POST['department_name']
    budget = request.POST['department_budget']
    dep = Department(name=name, budget=budget)
    dep.save()
    return HttpResponseRedirect(reverse('Bangazon:departments'))

def department_details(request, department_id):
    department_details = Department.objects.get(pk=department_id)
    context = {'department_details': department_details}
    return render(request, 'Bangazon/department_details.html', context)

# ==========================COMPUTERS=================================


def computers(request):
    computer_list = Computer.objects.all()
    context = {'computer_list': computer_list}
    return render(request, 'Bangazon/computers.html', context)


def computer_details(request, computer_id):
  computer = get_object_or_404(Computer, pk=computer_id)
  print("id", computer.id)
  context = {'computer': computer}
  return render(request, 'Bangazon/computer_details.html', context)

def computer_form(request):
    employees = Employee.objects.all
    context = {"employees": employees}
    return render(request, "Bangazon/computer_form.html", context)


def computer_new(request):
    computer = Computer(
        purchaseDate=request.POST['purchase'], model=request.POST['model'], manufacturer=request.POST['manufacturer'])
    computer.save()
    employee = Employee.objects.all(pk=request.POST['assignment'])
    relationship = Employee_Computer(employee=employee, computer=computer)
    relationship.save()
    return HttpResponseRedirect(reverse('Bangazon:computers'))

def computer_delete_confirm(request):
    computer= Computer.objects.get(pk=request.POST['computer_id'])
    is_assigned=computer.employee_set.all()
    assigned = False
    if len(is_assigned) > 0:
        assigned = True
    context = {'computer': computer,
                'assigned': assigned}
    print("context", context)
    return render(request, "Bangazon/computer_delete_confirm.html", context)

def computer_delete(request):
    computer= Computer.objects.get(pk=request.POST['computer_id'])
    computer.delete()
    return HttpResponseRedirect(reverse('Bangazon:computers'))


# ===========================TRAINING================================

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

def training_details(request, trainingprogram_id):
    training_program_details = get_object_or_404(TrainingProgram, id=trainingprogram_id)
    assignees = EmployeeTrainingProgram.objects.filter(trainingProgram_id=training_program_details.id)
    attendees = []
    for emp in assignees:
        person = Employee.objects.get(id=emp.id)
        attendees.append(person)
    context = {'training_program_details': training_program_details, 'attendees': attendees}
    return render(request, 'Bangazon/indiv_training_program.html', context)

def past_training_details(request, trainingprogram_id):
    training_program_details = get_object_or_404(TrainingProgram, id=trainingprogram_id)
    assignees = EmployeeTrainingProgram.objects.filter(trainingProgram_id=training_program_details.id)
    attendees = []
    for emp in assignees:
        person = Employee.objects.get(id=emp.id)
        attendees.append(person)
    context = {'training_program_details': training_program_details, 'attendees': attendees}
    return render(request, 'Bangazon/past_indiv_training_program.html', context)

def new_training_program_form(request):
    form = NewTrainingForm()
    return render(request, 'Bangazon/new_training_program_form.html', {'form': form})

def save_program(request):
    training = TrainingProgram(name=request.POST['training_name'], description=request.POST['training_description'], startDate=request.POST['training_startDate'], endDate=request.POST['training_endDate'], maxEnrollment=request.POST['training_maxEnrollment'])
    training.save()
    return HttpResponseRedirect(reverse('Bangazon:training_programs'))



def edit_training_details(request, pk):
    training_program_details = get_object_or_404(TrainingProgram, id=pk)
    form = NewTrainingForm(initial={'training_name': training_program_details.name, 'training_description': training_program_details.description, 'training_startDate': training_program_details.startDate, 'training_endDate': training_program_details.endDate, 'training_maxEnrollment': training_program_details.maxEnrollment})
    return render(request, 'Bangazon/edit_training.html', {'form': form, "id": pk})


def update_program(request, pk):
    TrainingProgram.objects.filter(id=pk).update(name = request.POST['training_name'], description = request.POST['training_description'], startDate = request.POST['training_startDate'], endDate = request.POST['training_endDate'], maxEnrollment = request.POST['training_maxEnrollment'])
    response = redirect('../Training')
    return response

def training_delete(request, pk):
    training = TrainingProgram.objects.get(id=pk)
    training.delete()
    return HttpResponseRedirect(reverse('Bangazon:training_programs'))