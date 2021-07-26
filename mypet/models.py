import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

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
                                  upload_to=f"images/{timezone.localdate()}",
                                  processors=[ResizeToFit(300, 300, upscale=False)],
                                  format='JPEG')

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        try:
            old = Pet.objects.get(id=self.id)
            if old.picture != self.picture:
                old.picture.delete()
        except (Pet.DoesNotExist, RecursionError):
            pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)
