from mixer.backend.django import mixer
import pytest

from accounts.models import UserAuth
from mycalendar.models import Event
from mypet.models import Pet


@pytest.mark.django_db
class TestModels:
    """Class that tests mycalendar models"""

    def test_event_model(self):
        """Test a new event is in database"""

        event_reason = mixer.blend(Event, reason='Vaccin')
        assert event_reason.reason == 'Vaccin'
        assert Event.objects.filter(reason='Vaccin').exists() is True
        assert Event.objects.count() == 1

    def test_str_event(self):
        """Test the string method from event model"""
        user = UserAuth.objects.create(username="Leonard",
                                       password="Testing1234",
                                       email="test@test.com")

        user_id = UserAuth.objects.get(id=user.id)

        pet = Pet.objects.create(user_id=user_id.id,
                                 species="cat", gender="male",
                                 birth_date="2021-05-05",
                                 name="Felix")

        event = Event.objects.create(user_id_id=user_id.id,
                                     date="2021-05-05 14:42:00+02",
                                     pet_name_id=pet.id,
                                     reason="Vaccin",
                                     mail_alert=False)

        assert str(event) == "{}, {}, {}, {}".format(event.user_id.username,
                                                     event.date,
                                                     event.pet_name.name,
                                                     event.mail_alert)
