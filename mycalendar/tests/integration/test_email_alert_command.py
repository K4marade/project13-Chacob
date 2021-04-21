from mixer.backend.django import mixer
from mycalendar.management.commands.email_alert import Email
from mycalendar.models import Event
from accounts.models import UserAuth
from django.core import mail
from datetime import datetime
import pytest


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
        user = mixer.blend(UserAuth, id=1,
                           username="Leonard",
                           email="testleonard@test.com")

        assert user.username == "Leonard"

        # Assert user is in database
        assert len(UserAuth.objects.filter(email="testleonard@test.com")) == 1

        # Create a user event
        user_event = mixer.blend(Event,
                                 date=datetime.now(),
                                 pet_name="Felix",
                                 reason="Vaccin",
                                 user_id_id=1,
                                 mail_alert=True)

        assert user_event.reason == "Vaccin"

        # Assert user event is in database with alert True
        assert len(Event.objects.filter(pet_name="Felix")) == 1

        self.mail.send_mail_alert()

        # Assert email is sent
        assert len(mail.outbox) == 1
        # Assert the body of the mail contains the pet name
        assert user_event.pet_name in mail.outbox[0].body

    def test_alert_mail_not_sent(self):
        """Method that tests no email is sent to the user
        after he did not subscribed to email alert for its appointment"""

        # Create a registered user
        user = mixer.blend(UserAuth, id=1,
                           username="Leonard",
                           email="testleonard@test.com")

        assert user.username == "Leonard"

        # Assert user is in database
        assert len(UserAuth.objects.filter(email="testleonard@test.com")) == 1

        # Create a user event with alert False
        user_event = mixer.blend(Event,
                                 date=datetime.now(),
                                 pet_name="Felix",
                                 reason="Vaccin",
                                 user_id_id=1,
                                 mail_alert=False)

        assert user_event.mail_alert is False

        assert len(Event.objects.filter(pet_name="Felix")) == 1

        self.mail.send_mail_alert()

        # Assert no mail is sent
        assert len(mail.outbox) == 0
