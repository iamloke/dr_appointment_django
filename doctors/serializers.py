from rest_framework import serializers
from doctors.models import *

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['user', 'specialization']
    
    def validate_user(self, value):
        if not value.is_doctor:
            raise serializers.ValidationError("Profile must be a doctor")
        return value

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name', 'description']