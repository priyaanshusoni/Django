from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "grade", "address"]
    search_fields = ["first_name"]
    list_filter = ["age", "address"]


admin.site.register(Student, StudentAdmin)
