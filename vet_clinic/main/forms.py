from .models import Owner, Pet, Doctor, Appointment
from django.forms import ModelForm
from django import forms

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'last_name', 'phone', 'email']

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'type', 'birth_date', 'gender']

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_time', 'reason']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }