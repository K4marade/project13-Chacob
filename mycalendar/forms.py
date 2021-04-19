from django.forms import ModelForm, DateTimeInput
from .models import Event
from django.utils.translation import gettext_lazy as _


class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {"date": DateTimeInput(attrs={"type": "datetime-local"},)}
        fields = ("date", "pet_name", "reason", "comment")
        labels = {"date": _("Date et Heure"),
                  "pet_name": _("Nom de mon animal"),
                  "reason": _("Motif"),
                  "comment": _("Commentaire")}
