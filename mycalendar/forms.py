from django.forms import ModelForm, DateTimeInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {'date': DateTimeInput(attrs={'type': 'datetime-local'})}
        fields = ('date', 'pet_name', 'reason', 'comment')
