from django.urls import path
from appointments.views import *

urlpatterns = [
    path('appointment/add/', AddAppointment.as_view(), name='add-appointment'),
    path('appointments/', AddAppointment.as_view(), name='all-appointment'),
    path('appointment/<int:pk>/', AddAppointment.as_view(), name='appointment'),
    path('appointment/delete/<int:pk>', DeleteAppointment.as_view(), name='delete-appointment'),
]