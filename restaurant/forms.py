from django.forms import ModelForm, BooleanField

from restaurant.models import Client, Booking


class StyleFormMixin:
    """Миксин для стилизации формы"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    """Форма редактирования клиента"""

    class Meta:
        model = Client
        fields = '__all__'


class BookingForm(StyleFormMixin, ModelForm):
    """Форма редактирования бронирования столика"""

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('owner',)
