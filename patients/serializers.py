from rest_framework import serializers
from patients.models import PatientProfile

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['user', 'phone', 'date_of_birth', 'medical_history']