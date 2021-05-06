from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


def validate_image(fieldfile_obj):
    """Function used to restrict file upload size"""

    filesize = fieldfile_obj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class Pet(models.Model):
    """Stores a single pet entry, related to :model:`accounts.UserAuth`."""

    SPECIES_CHOICE = [
        ("cat", "Chat"),
        ("dog", "Chien")
    ]
    GENDER_CHOICE = [
        ("male", "Mâle"),
        ("female", "Femelle "),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    birth_date = models.DateField()
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True, upload_to="images/", )  # validators=[validate_image])

    def __str__(self):
        return "{}".format(self.name)
