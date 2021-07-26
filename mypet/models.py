# from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


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
    picture = ProcessedImageField(null=True,
                                  blank=True,
                                  upload_to="images/",
                                  processors=[ResizeToFit(300, 300, upscale=False)],
                                  format='JPEG')

    def __str__(self):
        return "{}".format(self.name)
