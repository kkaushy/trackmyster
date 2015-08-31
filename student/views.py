from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from student.models import Student, Travel
from student.serializers import StudentSerializer, TravelSerializer

class StudentList(APIView):
    """
    List all students, or create a new student.
    """
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    """
    Retrieve, update or delete a student instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TravelList(APIView):
    """
    List all employees, or create a new employee.
    """
    def get(self, request, format=None):
        travels = Travel.objects.all()
        serializer = TravelSerializer(travels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TravelDetail(APIView):
    """
    Retrieve, update or delete a employee instance.
    """
    def get_object(self, pk):
        try:
            return Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        travel = self.get_object(pk)
        serializer = TravelSerializer(travel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        travel = self.get_object(pk)
        serializer = TravelSerializer(travel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        travel = self.get_object(pk)
        travel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
