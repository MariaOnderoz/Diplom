from django.contrib import admin

from restaurant.models import Client, Booking


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'visit_date', 'visit_time', 'number_of_guests', 'special_request', 'booking_status')
    search_fields = ('client__first_name', 'client__last_name', 'client__phone_number', 'client__email')
    list_filter = ('booking_status', 'visit_date')
