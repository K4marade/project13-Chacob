# from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput
from .models import Pet
from django.utils.translation import gettext_lazy as _


class AddPetForm(ModelForm):
    class Meta:
        model = Pet
        widgets = {"birth_date": DateInput(attrs={"type": "date"})}
        fields = ("species", "gender", "birth_date", "name", "picture")
        labels = {"species": _("Espèce"),
                  "gender": _("Sexe"),
                  "birth_date": _("Date de naissance"),
                  "name": _("Nom de mon animal"),
                  "picture": _("Photo de profile")}

    # def clean_picture(self):
    #     data = self.cleaned_data['picture'].size
    #     megabyte_limit = 5.0
    #     if data > megabyte_limit * 1024 * 1024:
    #         raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    #     return data


class EditPetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ("species", "gender", "name", "picture")
        labels = {"species": _("Espèce"),
                  "gender": _("Sexe"),
                  "name": _("Nom de mon animal"),
                  "picture": _("Photo de profile")}

    # def clean_picture(self):
    #     data = self.cleaned_data['picture'].size
    #     megabyte_limit = 5.0
    #     if data > megabyte_limit * 1024 * 1024:
    #         raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    #     return data
