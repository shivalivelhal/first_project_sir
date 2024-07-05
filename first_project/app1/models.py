from django.db import models

# Create your models here.


class Employee(models.Model):
    # id 
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_num = models.IntegerField(unique=True) # BigIntegerField
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    date_joined = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False, null=True)
    # date_modified = models.DateField(auto_now_add=True)
    # created_by = models.CharField(max_length=100)
    # deleted_by = models.CharField(max_length=100)

    


    def __str__(self):
        return f"{self.name} - {self.salary}"

    def __repr__(self):
        return str(self)

    class Meta:
        db_table = "employee"  # app1_employee
