from django.shortcuts import render
from .models import Employee

# Create your views here.
# business logic

# FBV
def get_employees(request):  # select * from employee;
    all_emps = Employee.objects.all()  # fetching data from database using django orm queries
    return render(request=request, template_name="employees.html", context={"emps": all_emps})


def create_employee(request):
    return render(request, "create_employee.html")


def get_employee(request):
    pass


def update_employee(request):
    pass


def delete_employee(request):
    pass
