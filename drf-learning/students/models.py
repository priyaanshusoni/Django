from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(100)])

    def __str__(self):
        return self.name
