from rest_framework import serializers
from schedules.models import *

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['doctor', 'shift', 'date']

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['name', 'start_time', 'end_time']