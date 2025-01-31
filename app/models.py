from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Patient(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return str(self.name.username)

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)  # E.g., 'Monday', 'Tuesday', etc.
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ['doctor', 'day_of_week', 'start_time']

    def __str__(self):
        return f"{self.doctor} - {self.day_of_week}: {self.start_time} to {self.end_time}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'),('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )
    reason = models.TextField()

    class Meta:
        unique_together = ['patient', 'appointment_time']



    def __str__(self):
        return f"Appointment with {self.doctor} for {self.patient} on {self.appointment_time}"
    
    def get_absolute_url(self):
        return reverse('appoint_view', kwargs={'pk': self.pk})

