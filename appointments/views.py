
from django.shortcuts import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import *
from appointments.serializers import *
from appointments.models import *

# Appointment CRUD
class AddAppointment(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Appointment added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                appointment = Appointment.objects.get(pk=pk)
                serializer = AppointmentSerializer(schedule)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except appointment.DoesNotExist:
                return Response({"message": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            appointments = Appointment.objects.all()
            serializer = AppointmentSerializer(schedules, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteAppointment(APIView):
    def delete(self, request, pk, format=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
            appointment.delete()
            return Response({"message":"Appointment removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response({"message":"Appointment not found"},status=status.HTTP_404_NOT_FOUND)

# WOA
def optimize_schedule_view(request):
    doctors = DoctorProfile.objects.all()
    schedules = Schedule.objects.all()

    optimizer = AppointmentOptimization()

    optimizer.objective_function(doctors, schedules)

    return render(request, 'appointments/optimized_schedule.html')