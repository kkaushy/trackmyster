from rest_framework import serializers
from student.models import Student, Bus, Activity
from rest_framework_mongoengine.serializers import DocumentSerializer

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus


class ActivitySerializer(DocumentSerializer):
    class Meta:
        model = Activity

