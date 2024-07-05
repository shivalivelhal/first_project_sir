import datetime

from app1.models import Employee
from django.db.models import Avg

# exec(open(r'E:\Python-B11\B11_Practice\Django_Framework\first_project\app1\db_shell.py').read())


# CRUD -- Create Read Update Delete

# Read All
# all_emps = Employee.objects.all() # [0:3]  # 0 1 2
# print(all_emps)
#

# for emp in all_emps:
#     print(emp.__dict__)


# Single read
# try:
#     emp = Employee.objects.get(id=4)
#     print(emp)
# except Employee.DoesNotExist:
#     print("Employee with given id does not exist in database.")

# create

# 1 way
# emp = Employee(
#     name="D",
#     email="d@gmail.com",
#     mobile_num=144178569,
#     designation="Tester",
#     salary=38457,
# )
# emp.save()

# 2 way
# Employee.objects.create(
#     name="E",
#     email="e@gmail.com",
#     mobile_num=145178569,
#     designation="Product Manager",
#     salary=658457,
# )


# update

# try:
#     emp_obj = Employee.objects.get(id=1)
#     emp_obj.salary = 45872
#     emp_obj.email = "aa"

#     emp_obj.save()
# except Employee.DoesNotExist:
#     print("Employee with given id does not exist in database.")


# delete

# try:
#     emp_obj = Employee.objects.get(id=6)
#     emp_obj.delete()
# except Employee.DoesNotExist:
#     print("Employee with given id does not exist in database.")

# emp = Employee.objects.filter(email="aaaa@gmail.com")
# emp = Employee.objects.filter(salary=45872)
# emp = Employee.objects.filter(designation__startswith="Python")  # 2 baar underscore
# emp = Employee.objects.filter(designation__endswith="r")  # 2 baar underscore

# emp = Employee.objects.filter(salary__lte=40000)  # 2 baar underscore

# print(emp)


# emp = Employee.objects.get(email="a@gmail.com")
# print(emp)

# employees_ordered_by_salary = Employee.objects.order_by('-salary')


# avg_salary = Employee.objects.aggregate(Avg("salary"))
# print(avg_salary)

# mid_salary_employees = Employee.objects.filter(salary__gte=50000, salary__lte=80000)
# and                  salary >= 50000   and salary <= 80000

# top_2_highest_paid = Employee.objects.order_by("-salary")[:2] # 0 1   [start:stop:stepsize]
# print(top_2_highest_paid)


# [45872, 654780, 35987, 38457]
# [654780, 45872, 38457, 35987][:2]  # 0 1

# non_developers = Employee.objects.filter(salary__gte=450000).exclude(designation="Developer")

# 54000  -- engineer
# 89000  -- tester
# 78450 --- developer

# distinct_designations = Employee.objects.values('designation').distinct()
# print(distinct_designations)


# from django.utils import timezone
# five_years_ago = timezone.now() - timezone.timedelta(days=5*365)
# print(five_years_ago)
# long_term_employees = Employee.objects.filter(date_joined__lt=five_years_ago)

# from django.db.models.functions import Substr

# distinct_email_domains = Employee.objects.annotate(
#     domain=Substr('email', Position('@', 'email') + 1)
# ).values('domain').distinct().count()

# from django.db.models import FloatField
# from django.db.models.functions import Cast

# total_employees = Employee.objects.count()
# top_10_percentile_index = int(total_employees * 0.5)
# top_10_percentile_salaries = list(Employee.objects.order_by('-salary').values_list('salary', flat=True)[:top_10_percentile_index])
# top_10_percentile_salary_value = top_10_percentile_salaries[-1] if top_10_percentile_salaries else 0
# top_10_percentile_employees = Employee.objects.filter(salary__gte=top_10_percentile_salary_value)
# print(top_10_percentile_employees)


# https://github.com/geekcomputers/Python/blob/master/Translator/translator.py