from django.forms import ModelForm, DateInput
from .models import Pet
from django.utils.translation import gettext_lazy as _


class PetForm(ModelForm):
    class Meta:
        model = Pet
        widgets = {"birth_date": DateInput(attrs={"type": "date"})}
        fields = ("species", "gender", "birth_date", "name", "picture")
        labels = {"species": _("Espèce"),
                  "gender": _("Sexe"),
                  "birth_date": _("Date de naissance"),
                  "name": _("Nom de mon animal"),
                  "picture": _("Ajouter une photo")}
