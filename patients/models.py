from django.db import models
from users.models import CustomUser

class PatientProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username