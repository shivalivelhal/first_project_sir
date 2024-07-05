from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
# business logic


# FBV
def get_employees(request):  # select * from employee;
    all_emps = (
        Employee.objects.all()  # is_deleted=False
    )  # fetching data from database using django orm queries
    return render(
        request=request, template_name="employees.html", context={"emps": all_emps}
    )


def create_employee(request):
    if request.method == "POST":
        print(request.POST)
        emp_name = request.POST.get("nm")
        emp_email = request.POST.get("em")
        emp_mob = request.POST.get("mb")
        emp_desn = request.POST.get("desn")
        emp_salary = request.POST.get("sal")

        if not request.POST.get("id"):
            Employee.objects.create(
                name=emp_name,
                email=emp_email,
                mobile_num=emp_mob,
                designation=emp_desn,
                salary=emp_salary,
            )
        else:
            emp = Employee.objects.get(id=request.POST.get("id"))
            emp.name = emp_name
            emp.email = emp_email
            emp.mobile_num = emp_mob
            emp.designation = emp_desn
            emp.salary = emp_salary
            emp.save()

        return redirect("get_emps")
    elif request.method == "GET":
        return render(request, "create_employee.html")


def get_employee(request, eid):
    emp = Employee.objects.get(id=eid)
    return render(request, "create_employee.html", {"single_emp": emp})


def update_employee(request, eid):
    pass


def delete_employee(request, eid):
    pass
