import pytest

from django.core import mail
from django.utils import timezone

from mixer.backend.django import mixer
from mycalendar.management.commands.email_alert import Email
from mycalendar.models import Event
from accounts.models import UserAuth
from mypet.models import Pet


@pytest.mark.django_db
class TestCommand:
    """Class that tests personalised alert email command"""

    def setup_class(self):
        """Method that sets tests parameters"""
        # self.event = Event()
        self.mail = Email()

    def test_alert_mail_is_sent(self):
        """Method that tests if an email is sent to the user
        after he subscribed to email alert for its appointment"""

        # Create a registered user
        user = mixer.blend(UserAuth,
                           username="Leonard",
                           email="testleonard@test.com")

        assert user.username == "Leonard"

        # Create a pet
        pet = mixer.blend(Pet,
                          user=UserAuth.objects.get(id=user.id),
                          name="Felix")

        assert pet.name == "Felix"

        # Assert user and pet is in database
        assert len(UserAuth.objects.filter(email="testleonard@test.com")) == 1
        assert len(Pet.objects.filter(id=1)) == 1

        # Create a user event
        user_event = mixer.blend(Event,
                                 date=timezone.now(),
                                 reason="Vaccin",
                                 pet_name=Pet.objects.get(name="Felix"),
                                 user_id_id=UserAuth.objects.get(id=user.id).id,
                                 mail_alert=True)

        assert user_event.reason == "Vaccin"

        # Assert user event is in database
        assert len(Event.objects.filter(reason="Vaccin")) == 1

        self.mail.send_mail_alert()

        # Assert email is sent
        assert len(mail.outbox) == 1
        # Assert the body of the mail contains the pet name
        assert str(user_event.pet_name) in mail.outbox[0].body

    def test_alert_mail_not_sent(self):
        """Method that tests no email is sent to the user
        after he did not subscribed to email alert for its appointment"""

        # Create a registered user
        user = mixer.blend(UserAuth,
                           username="Leonard",
                           email="testleonard@test.com")

        assert user.username == "Leonard"

        # Assert user is in database
        assert len(UserAuth.objects.filter(email="testleonard@test.com")) == 1

        # Create a pet
        mixer.blend(Pet,
                    user=UserAuth.objects.get(id=user.id),
                    name="Felix")

        # Create a user event with alert False
        user_event = mixer.blend(Event,
                                 date=timezone.now(),
                                 reason="Vaccin",
                                 pet_name=Pet.objects.get(name="Felix"),
                                 user_id_id=UserAuth.objects.get(id=user.id).id,
                                 mail_alert=False)

        assert user_event.mail_alert is False

        assert len(Event.objects.filter(reason="Vaccin")) == 1

        self.mail.send_mail_alert()

        # Assert no mail is sent
        assert len(mail.outbox) == 0
