# from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from PIL import Image


# def validate_image(fieldfile_obj):
#     """Function used to restrict file upload size"""
#
#     filesize = fieldfile_obj.file.size
#     megabyte_limit = 5.0
#     if filesize > megabyte_limit * 1024 * 1024:
#         raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


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

    def save(self, *args, **kwargs):
        """Function that resizes an image if size is over 1024 px"""

        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)

        if img.height > 1024 or img.width > 1024:
            output_size = (img.height/2, img.width/2)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    def __str__(self):
        return "{}".format(self.name)
