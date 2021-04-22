from django.forms import ModelForm, DateInput
from .models import Pet


class PetForm(ModelForm):
    class Meta:
        model = Pet
        widgets = {"birth_date": DateInput(attrs={"type": "date"})}
        fields = ("species", "gender", "birth_date", "name", "picture")
