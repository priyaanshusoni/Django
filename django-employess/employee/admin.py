from django.contrib import admin
from django.db import models
from .models import Department, Employee

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "get_full_name",
        "designation",
        "is_active",
    ]
    list_filter = ["manager"]
    search_fields = ["first_name", "email"]
    list_editable = ["is_active"]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
