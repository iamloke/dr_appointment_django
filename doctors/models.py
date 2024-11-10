from django.db import models
from accounts.models import CustomUser

class Doctor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    # profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # specialization_icon = models.ImageField(upload_to='specialization_icons/', blank=True, null=True)

    def __str__(self):
        return self.name