from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'studentName',
            'dob',
            'gender',
            'grade',
            'section',
            'aadharID',
            'existingComorbidites',
            'bloodGroup',
            'vaccination'
        )
