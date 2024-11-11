from rest_framework import serializers
from appointments.models import *

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'schedule', 'appointment_time']