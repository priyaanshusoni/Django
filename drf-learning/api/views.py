from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .serializers import StudentSerializer
from students.models import Student

# Create your views here.


# def index(request):
#     return JsonResponse({"id": 1, "name": "priyanshu", "orders": []})


@api_view(["GET", "POST"])
def StudentListView(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        print(f"serializer data is {serializer.data}")

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":

        # take payload from request
        serializer = StudentSerializer(data=request.data)

        # validate that payload
        # put it into the db

        # return the response

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def StudentDetailView(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "GET":
        serializer = StudentSerializer(student)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
