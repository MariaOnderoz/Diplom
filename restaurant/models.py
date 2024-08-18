from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    """Модель клиента"""

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Booking(models.Model):
    """Модель бронирования"""

    statuses = [
        ('Сonfirmed', 'Подтверждено'),
        ('Rejected', 'Отклонено'),
        ('Awaiting confirmation', 'Ожидает подтверждения'),
    ]

    timing = [
        (0, '19:00'),
        (1, '19:30'),
        (2, '20:00'),
        (3, '20:30'),
        (4, '21:00'),
        (5, '21:30'),
        (6, '22:00'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    visit_date = models.DateField(default=date.today, verbose_name='Дата бронирования')
    visit_time = models.TimeField(choices=timing, verbose_name='Время бронирования')
    number_of_guests = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Количество гостей')
    special_request = models.TextField(verbose_name='Особые пожелания', **NULLABLE)
    booking_status = models.CharField(max_length=50, choices=statuses, verbose_name='Статус бронирования')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.client} - {self.visit_date} {self.visit_time}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
