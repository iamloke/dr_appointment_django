
from django.shortcuts import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import *
from doctors.serializers import *
from doctors.models import *

# DoctorProfile CRUD
class AddDoctorProfile(APIView):
    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Doctor profile added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                doctor_profile = DoctorProfile.objects.get(pk=pk)
                serializer = DoctorProfileSerializer(doctor_profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except DoctorProfile.DoesNotExist:
                return Response({"message": "Doctor profile not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            doctor_profiles = DoctorProfile.objects.all()
            serializer = DoctorProfileSerializer(doctor_profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteDoctorProfile(APIView):
    def delete(self, request, pk, format=None):
        try:
            doctor_profile = DoctorProfile.objects.get(pk=pk)
            doctor_profile.delete()
            return Response({"message":"Doctor profile removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        except DoctorProfile.DoesNotExist:
            return Response({"message":"Doctor profile not found"},status=status.HTTP_404_NOT_FOUND)

# Specialization CRUD
class AddSpecialization(APIView):
    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Specialization added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                specialization = Specialization.objects.get(pk=pk)
                serializer = SpecializationSerializer(specialization)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PatientProfile.DoesNotExist:
                return Response({"message": "Doctor profile not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            specializations = Specialization.objects.all()
            serializer = SpecializationSerializer(specializations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteSpecialization(APIView):
    def delete(self, request, pk, format=None):
        try:
            specialization = Specialization.objects.get(pk=pk)
            specialization.delete()
            return Response({"message":"Specialization removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Specialization.DoesNotExist:
            return Response({"message":"Specialization not found"},status=status.HTTP_404_NOT_FOUND)
