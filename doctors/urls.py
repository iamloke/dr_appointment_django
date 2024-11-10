from django.urls import path
from doctors.views import *

urlpatterns = [
    path('doctor/profile/add/', AddDoctorProfile.as_view(), name='add-doctor-profile'),
    path('doctor/profiles/', AddDoctorProfile.as_view(), name='all-doctor-profile'),
    path('doctor/profile/<int:pk>/', AddDoctorProfile.as_view(), name='doctor-profile'),
    path('doctor/profile/delete/<int:pk>', DeleteDoctorProfile.as_view(), name='delete-doctor-profile'),

    path('specilization/add/', AddSpecialization.as_view(), name='add-specilization'),
    path('specilizations/', AddSpecialization.as_view(), name='all-specilization'),
    path('specilization/<int:pk>/', AddSpecialization.as_view(), name='specilization'),
    path('specilization/delete/<int:pk>', DeleteSpecialization.as_view(), name='delete-specilization'),
]