"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("get-employees/", views.get_employees, name="get_emps"),  # petname: get_emmps
    path("create-employee/", views.create_employee, name="create_emp"),
    path("get-employee/<int:eid>/", views.get_employee, name="get_emp"),
    path("update-employee/<int:eid>/", views.update_employee, name="update_emp"),
    path("delete-employee/<int:eid>/", views.delete_employee, name="delete_emp"),
]
