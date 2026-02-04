from .models import Owner, Pet, Doctor, Appointment
from django.forms import ModelForm
from django import forms

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