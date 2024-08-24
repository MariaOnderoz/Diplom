from django.forms import ModelForm, BooleanField

from restaurant.models import Booking, Table


class StyleFormMixin:
    """Миксин для стилизации формы"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class TableForm(StyleFormMixin, ModelForm):
    """Форма редактирования столика"""

    class Meta:
        model = Table
        fields = '__all__'


class BookingForm(StyleFormMixin, ModelForm):
    """Форма редактирования бронирования столика"""

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('owner', 'booking_status', )
