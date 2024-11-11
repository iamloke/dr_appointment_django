from django.db import models
from doctors.models import DoctorProfile

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    shift = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.shift.name} - {self.shift.start_time} to {self.shift.end_time} on {self.date}"
        
class Shift(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")

    def __str__(self):
        return f"{self.name} - {self.start_time} - {self.end_time}"