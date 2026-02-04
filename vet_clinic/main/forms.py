from .models import Owner, Pet, Doctor, Appointment
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'last_name', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
        }

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'type', 'birth_date', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
            'type': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 bg-white focus:ring-2 focus:ring-purple-400'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 bg-white focus:ring-2 focus:ring-purple-400'
            }),
        }

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_time', 'reason']
        widgets = {
            'doctor': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 bg-white focus:ring-2 focus:ring-purple-400'
            }),
            'appointment_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
            'appointment_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
            'reason': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-purple-400'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        date = cleaned_data.get('appointment_date')
        time = cleaned_data.get('appointment_time')
    
        if doctor and date and time:
            exists = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=date,
                appointment_time=time
            ).exists()
            if exists:
                raise ValidationError(
                    "На это время у данного врача уже есть запись. Пожалуйста, выберите другое время."
                )