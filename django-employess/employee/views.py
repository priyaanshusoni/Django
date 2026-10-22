from django.shortcuts import render
from django.http import HttpResponse


from .models import Employee


# Create your views here.
def index(request):
    employees = Employee.objects.all()

    context = {"employees": employees}
    return render(request, "home.html", context)
