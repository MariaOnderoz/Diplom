from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from config import settings
from restaurant.forms import TableForm, BookingForm
from restaurant.models import Table, Booking
from users.models import User


class HomePage(TemplateView):
    """Контроллер главной страницы"""

    template_name = 'restaurant/home.html'


class ContactsView(TemplateView):
    """Контроллер страницы контактов"""

    template_name = 'restaurant/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Классы для клиентов


class TableCreateView(CreateView):
    """Контроллер создания нового стола"""

    model = Table
    form_class = TableForm
    success_url = reverse_lazy('restaurant:table_list')

    def form_valid(self, form):
        table = form.save()
        user = self.request.user
        table.owner = user
        table.save()
        return super().form_valid(form)


class TableListView(ListView):
    """Контроллер списка всех столов"""

    model = Table

    # def get_queryset(self):
    #     user = self.request.user
    #     return super().get_queryset().filter(owner=user)


class TableDetailView(DetailView):
    """Контроллер детального просмотра стола"""

    model = Table

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class TableUpdateView(UpdateView):
    """Контроллер редактирования стола"""
    model = Table
    form_class = TableForm
    success_url = reverse_lazy('restaurant:table_list')


class TableDeleteView(DeleteView):
    """Контроллер удаления стола"""

    model = Table
    success_url = reverse_lazy('restaurant:table_list')


# Классы для бронирования


class BookingCreateView(CreateView):
    """Контроллер создания нового бронирования"""

    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy('restaurant:booking_list')

    def form_valid(self, form):
        booking = form.save()
        user = self.request.user
        booking.owner = user
        booking.save()
        return super().form_valid(form)


class BookingListView(ListView):
    """Контроллер списка всех бронирований"""

    model = Booking

    # def get_queryset(self):
    #     user = self.request.user
    #     return super().get_queryset().filter(owner=user)


class BookingDetailView(DetailView):
    """Контроллер детального просмотра бронирования"""

    model = Booking

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        return context_data


class BookingUpdateView(UpdateView):
    """Контроллер редактирования бронирования"""

    model = Booking
    form_class = BookingForm

    def get_success_url(self):
        return reverse_lazy('restaurant:booking_detail', args=[self.kwargs.get('pk')])


class BookingDeleteView(DeleteView):
    """Контроллер удаления бронирования"""

    model = Booking
    success_url = reverse_lazy('restaurant:booking_list')
