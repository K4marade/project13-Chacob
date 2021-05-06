from django.forms import ModelForm, DateTimeInput, Textarea

from mypet.models import Pet
from .models import Event
from django.utils.translation import gettext_lazy as _


class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {"date": DateTimeInput(attrs={"type": "datetime-local",
                                                "placeholder": "jj/mm/aaaa hh:mm"}),
                   "comment": Textarea(attrs={"rows": 4, "cols": 15},)}
        fields = ("date", "pet_name", "reason", "comment", "mail_alert")
        labels = {"date": _("Date et Heure"),
                  "pet_name": _("Nom de mon animal"),
                  "reason": _("Motif"),
                  "comment": _("Commentaire"),
                  "mail_alert": _("Recevoir un rappel par email")}

    def __init__(self, user, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["pet_name"].queryset = Pet.objects.filter(user=user)
        self.fields["pet_name"].empty_label = "Aucun"
