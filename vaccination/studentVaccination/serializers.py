from rest_framework import serializers
from .models import StudentVaccination

class StudentVaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentVaccination
        fields = (
            'id',
            'vaccinationDate',
            'dosage',
            'vaccinationStatus',
            'student',
            'vaccine'
        )
