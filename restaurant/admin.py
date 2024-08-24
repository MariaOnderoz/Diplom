from django.contrib import admin

from restaurant.models import Booking, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'seats_count', 'is_available')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'visit_date', 'visit_time', 'number_of_guests', 'booking_status')
