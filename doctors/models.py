from django.db import models
from users.models import CustomUser

class DoctorProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    specialization = models.ForeignKey('Specialization', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.user.is_doctor:
            raise ValidationError("User is not a doctor.")

    def __str__(self):
        return self.user.username

class Specialization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name