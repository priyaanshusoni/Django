from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.functions import Lower

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
        return self.name
