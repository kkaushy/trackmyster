from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from student.models import Student, Bus, Activity
from student.serializers import StudentSerializer, BusSerializer, ActivitySerializer

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


class BusList(APIView):
    """
    List all employees, or create a new Bus.
    """
    def get(self, request, format=None):
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusDetail(APIView):
    """
    Retrieve, update or delete a Bus instance.
    """
    def get_object(self, pk):
        try:
            return Bus.objects.get(pk=pk)
        except Bus.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = BusSerializer(bus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = BusSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActivityList(APIView):
    """
    List all employees, or create a new Activity.
    """
    def get(self, request, format=None):
        Activities = Activity.objects.all()
        serializer = ActivitySerializer(Activities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityDetail(APIView):
    """
    Retrieve, update or delete a Activity instance.
    """
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = ActivitySerializer(bus)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     Activity = self.get_object(pk)
    #     serializer = ActivitySerializer(bus, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     Activity = self.get_object(pk)
    #     Activity.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
