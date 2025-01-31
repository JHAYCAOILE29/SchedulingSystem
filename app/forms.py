from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['date_of_birth', 'email', 'phone_number', 'address'] 

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        patient = super().save(commit=False)
        if self.user:  
            patient.name = self.user
        if commit:
            patient.save()
        return patient
