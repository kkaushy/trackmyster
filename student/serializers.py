from rest_framework import serializers
from student.models import Student, Travel

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel