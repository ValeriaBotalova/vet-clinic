from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Pet
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

            messages.success(request,'Запись успешно создана. Мы ждём вас на приёме!')
            return redirect('main')
    else:
        owner_form = OwnerForm(prefix='owner')
        pet_form = PetForm(prefix='pet')
        appointment_form = AppointmentForm(prefix='appointment')

    return render(request, 'main/appointment.html', {
        'owner_form': owner_form,
        'pet_form': pet_form,
        'appointment_form': appointment_form,
    })

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'main/pet_list.html', {'pets': pets})

def med_card(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    appointments = pet.appointments.all().order_by('-appointment_date')
    return render(request, 'main/med_card.html', {
        'pet': pet,
        'appointments': appointments
    })
