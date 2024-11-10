
from django.shortcuts import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import *
from patients.serializers import *
from patients.models import *

class AddPatientProfile(APIView):
    def post(self, request):
        serializer = PatientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Patient profile added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                patient_profile = PatientProfile.objects.get(pk=pk)
                serializer = PatientProfileSerializer(patient_profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PatientProfile.DoesNotExist:
                return Response({"message": "Patient profile not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            patient_profiles = PatientProfile.objects.all()
            serializer = PatientProfileSerializer(patient_profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DeletePatientProfile(APIView):
    def delete(self, request, pk, format=None):
        try:
            patient_profile = PatientProfile.objects.get(pk=pk)
            patient_profile.delete()
            return Response({"message":"Patient profile removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        except PatientProfile.DoesNotExist:
            return Response({"message":"Patient profile not found"},status=status.HTTP_404_NOT_FOUND)
    
