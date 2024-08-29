from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Table(models.Model):
    """Модель стола"""

    table_number = models.PositiveIntegerField(primary_key=True, verbose_name='Номер стола')
    seats_count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(6)], verbose_name='Количество мест')
    is_available = models.BooleanField(default=True, verbose_name='Свободен')
    image = models.ImageField(upload_to='media/images/', verbose_name='Схема столов', **NULLABLE)


class Booking(models.Model):
    """Модель бронирования"""

    statuses = [
        ('Сonfirmed', 'Подтверждено'),
        ('Rejected', 'Отклонено'),
        ('Awaiting confirmation', 'Ожидает подтверждения'),
    ]

    timing = [
        ('0', '19:00'),
        ('1', '19:30'),
        ('2', '20:00'),
        ('3', '20:30'),
        ('4', '21:00'),
        ('5', '21:30'),
        ('6', '22:00'),
    ]

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', **NULLABLE)
    email = models.EmailField(verbose_name='Электронная почта', **NULLABLE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='Номер стола', **NULLABLE)
    visit_date = models.DateField(default=date.today, verbose_name='Дата бронирования')
    visit_time = models.TimeField(choices=timing, verbose_name='Время бронирования', **NULLABLE)
    number_of_guests = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Количество гостей')
    special_request = models.TextField(verbose_name='Особые пожелания', **NULLABLE)
    booking_status = models.CharField(max_length=50, choices=statuses, verbose_name='Статус бронирования')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.booking_status}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

        constraints = [
            models.UniqueConstraint(fields=['visit_time', 'visit_date', 'table'], name='name of constraint')
        ]

