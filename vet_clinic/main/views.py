from pyexpat.errors import messages
from django.shortcuts import render
from .forms import OwnerForm, PetForm, AppointmentForm

def index(request):
    return render(request, 'main/main_page.html')

def appointment(request):
    if request.method == 'POST':
        owner_form = OwnerForm(request.POST, prefix='owner')
        pet_form = PetForm(request.POST, prefix='pet')
        appointment_form = AppointmentForm(request.POST, prefix='appointment')

        if owner_form.is_valid() and pet_form.is_valid() and appointment_form.is_valid():
            owner = owner_form.save()

            pet = pet_form.save(commit=False)
            pet.owner = owner
            pet.save()

            appointment = appointment_form.save(commit=False)
            appointment.pet = pet
            appointment.save()
    else:
        owner_form = OwnerForm(prefix='owner')
        pet_form = PetForm(prefix='pet')
        appointment_form = AppointmentForm(prefix='appointment')

    return render(request, 'main/appointment.html', {
        'owner_form': owner_form,
        'pet_form': pet_form,
        'appointment_form': appointment_form,
    })