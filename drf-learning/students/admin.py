from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ["name", "age"]


admin.site.register(Student, StudentAdmin)
