from django.urls import path
from restaurant.apps import RestaurantConfig
from restaurant.views import HomePage, TableCreateView, TableListView, TableDetailView, TableUpdateView, TableDeleteView, \
BookingListView, BookingCreateView, BookingDetailView, BookingUpdateView, BookingDeleteView, \
    ContactsView

app_name = RestaurantConfig.name

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('table/', TableListView.as_view(), name='table_list'),
    path('table/create/', TableCreateView.as_view(), name='table_create'),
    path('table/<int:pk>/', TableDetailView.as_view(), name='table_detail'),
    path('table/<int:pk>/update/', TableUpdateView.as_view(), name='table_update'),
    path('table/<int:pk>/delete/', TableDeleteView.as_view(), name='table_delete'),

    path('booking/', BookingListView.as_view(), name='booking_list'),
    path('booking/create/', BookingCreateView.as_view(), name='booking_create'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('booking/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]