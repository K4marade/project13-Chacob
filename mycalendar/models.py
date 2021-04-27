from django.db import models
from django.conf import settings


class Event(models.Model):
    """
    Stores a single event entry, related to :model:`accounts.UserAuth`.
    """

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date = models.DateTimeField()
    pet_name = models.ForeignKey('mypet.Pet', on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    comment = models.TextField(max_length=250, null=True, blank=True)
    mail_alert = models.BooleanField()

    def __str__(self):
        return "{}, {}, {}, {}".format(self.user_id, self.date, self.pet_name, self.mail_alert)
