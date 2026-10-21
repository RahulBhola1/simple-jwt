from django.http import request
from rest_framework.decorators import api_view
from .StudentSerializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Student
# Create your views here.

@api_view(['GET' , 'POST'])
def myfirstendpoint(request):
    if request.method == "GET":
        objs = Student.objects.all()
        return Response(StudentSerializer(objs ,many = True).data , status = status.HTTP_200_OK)

    if request.method == "POST":
        student = StudentSerializer(data = request.data)
        if student.is_valid():
            student.save()
            return Response(student.data , status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_202_ACCEPTED)
        