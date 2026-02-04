from django.contrib import admin
from .models import Owner, Pet, Doctor, Appointment

admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Doctor)
admin.site.register(Appointment)