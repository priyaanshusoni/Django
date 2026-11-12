from django.urls import path

from . import views

urlpatterns = [
    path("students", views.StudentListView),
    path("students/<int:pk>", views.StudentDetailView),
]
