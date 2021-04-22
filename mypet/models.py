from django.db import models
from django.conf import settings


class Pet(models.Model):
    SPECIES_CHOICE = [
        ("cat", "Cat")
    ]
    GENDER_CHOICE = [
        ("male", "Male"),
        ("female", "Female "),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    birth_date = models.DateField()
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")

