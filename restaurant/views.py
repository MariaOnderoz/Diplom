from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from restaurant.forms import ClientForm, BookingForm
from restaurant.models import Client, Booking


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


class ClientCreateView(CreateView):
    """Контроллер создания нового клиента"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('restaurant:home')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientListView(ListView):
    """Контроллер списка всех клиентов"""

    model = Client

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(owner=user)


class ClientDetailView(DetailView):
    """Контроллер детального просмотра клиента"""

    model = Client

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        return context_data


class ClientUpdateView(UpdateView):
    """Контроллер редактирования клиента"""

    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse_lazy('restaurant:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    """Контроллер удаления клиента"""

    model = Client
    success_url = reverse_lazy('restaurant:client_list')


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
