from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.functions import Lower

from django.contrib import admin

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="department_name_case_insensitive_unique",
                violation_error_message="Department already exists (case-insensitive match)",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.name}- {self.location}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    designation = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    joining_date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True
    )
    manager = models.ForeignKey(
        "self", blank=True, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.get_full_name()

    @admin.display(description="Name")
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
        constraints = [
            UniqueConstraint(
                Lower("email"),
                name="employee_email_case_insensitive_unique",
                violation_error_message="An employee with this email already exists",
            ),
        ]
