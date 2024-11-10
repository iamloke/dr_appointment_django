
from django.shortcuts import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import *
from schedules.serializers import *
from schedules.models import *

# Schedule CRUD
class AddSchedule(APIView):
    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Schedule added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                schedule = Schedule.objects.get(pk=pk)
                serializer = ScheduleSerializer(schedule)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Schedule.DoesNotExist:
                return Response({"message": "Schedule not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            schedules = Schedule.objects.all()
            serializer = ScheduleSerializer(schedules, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteSchedule(APIView):
    def delete(self, request, pk, format=None):
        try:
            schedule = Schedule.objects.get(pk=pk)
            schedule.delete()
            return Response({"message":"Schedule removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Schedule.DoesNotExist:
            return Response({"message":"Schedule not found"},status=status.HTTP_404_NOT_FOUND)

# Shift CRUD
class AddShift(APIView):
    def post(self, request):
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Shift added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                shift = Shift.objects.get(pk=pk)
                serializer = ShiftSerializer(specialization)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Shift.DoesNotExist:
                return Response({"message": "Shift not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            shifts = Shift.objects.all()
            serializer = ShiftSerializer(shifts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteShift(APIView):
    def delete(self, request, pk, format=None):
        try:
            shift = Shift.objects.get(pk=pk)
            shift.delete()
            return Response({"message":"Shift removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Shift.DoesNotExist:
            return Response({"message":"Shift not found"},status=status.HTTP_404_NOT_FOUND)
