from django.contrib import admin
from .models import Appointment, Patient, Doctor

admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Doctor)

