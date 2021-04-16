from django.db import models
from django.conf import settings


class Event(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date = models.DateTimeField()
    pet_name = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    comment = models.TextField(max_length=250)

    def __str__(self):
        return "{}, {}, {}".format(self.user_id, self.date, self.pet_name)
