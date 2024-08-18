from django.urls import path
from restaurant.apps import RestaurantConfig
from restaurant.views import HomePage, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, BookingListView, BookingCreateView, BookingDetailView, BookingUpdateView, BookingDeleteView, \
    ContactsView

app_name = RestaurantConfig.name

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('booking/', BookingListView.as_view(), name='booking_list'),
    path('booking/create/', BookingCreateView.as_view(), name='booking_create'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('booking/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]