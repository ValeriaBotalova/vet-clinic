from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?\d{10,15}$',
    message='Введите номер в формате +79998887766'
)


class Owner(models.Model):
    name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    phone = models.CharField(
        'Номер телефона',
        max_length=20,
        validators=[phone_validator]
    )
    email = models.EmailField('Электронная почта', max_length=254)
    def __str__(self):
        return f'{self.last_name} {self.name}'
    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

class Doctor(models.Model):
    name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    specialization = models.CharField('Профиль', max_length=100)
    def __str__(self):
        return f'{self.last_name} {self.name}'
    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

class Pet(models.Model):
    name = models.CharField('Имя питомца', max_length=100)
    class Type(models.TextChoices):
        CAT = 'cat', 'Кошка'
        DOG = 'dog', 'Собака'
        BIRD = 'bird', 'Птица'
        BUNNY = 'bunny', 'Кролик'

    type = models.CharField(
        max_length=20,
        choices=Type.choices
    )
    birth_date = models.DateField()
    class Gender(models.TextChoices):
        FEMALE = 'female', 'Женский'
        MALE = 'male', 'Мужской'

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='pets'
    )
    def __str__(self):
        return f'{self.get_type_display()} {self.name} {self.birth_date}'
    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

class Appointment(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField('Дата приема')
    appointment_time = models.TimeField('Время приема')
    reason = models.CharField('Причина визита', max_length=255)
    def __str__(self):
        return f'{self.pet.name} — {self.appointment_date} {self.appointment_time}'
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


