from django.urls import path
from patients.views import *

urlpatterns = [
    path('patient/profile/add/', AddPatientProfile.as_view(), name='add-patient-profile'),
    path('patient/profiles/', AddPatientProfile.as_view(), name='all-patient-profile'),
    path('patient/profile/<int:pk>/', AddPatientProfile.as_view(), name='patient-profile'),
    path('patient/profile/<int:pk>', DeletePatientProfile.as_view(), name='delete-patient-profile')
]