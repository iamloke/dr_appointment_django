from django.db import models
from doctors.models import DoctorProfile
from patients.models import PatientProfile
from schedules.models import Schedule

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.appointment_time < '09:00:00' or self.appointment_time > '17:00:00':
            raise ValidationError('Appointment time must be between 9:00 AM and 5:00 PM')

    def __str__(self):
        return f"Appointment for {self.patient.name} with {self.schedule.doctor.name} on {self.schedule.date} at {self.appointment_time}"