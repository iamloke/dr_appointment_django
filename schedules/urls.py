from django.urls import path
from schedules.views import *

urlpatterns = [
    path('schedule/add/', AddSchedule.as_view(), name='add-doctor-profile'),
    path('schedules/', AddSchedule.as_view(), name='all-doctor-profile'),
    path('schedule/<int:pk>/', AddSchedule.as_view(), name='doctor-profile'),
    path('schedule/delete/<int:pk>', DeleteSchedule.as_view(), name='delete-doctor-profile'),

    path('shift/add/', AddShift.as_view(), name='add-specilization'),
    path('shifts/', AddShift.as_view(), name='all-specilization'),
    path('shift/<int:pk>/', AddShift.as_view(), name='specilization'),
    path('shift/delete/<int:pk>', DeleteShift.as_view(), name='delete-specilization'),
]