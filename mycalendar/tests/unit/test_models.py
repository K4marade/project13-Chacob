from mixer.backend.django import mixer
import pytest
from mycalendar.models import Event


@pytest.mark.django_db
class TestModels:
    """Class that tests mycalendar models"""

    def test_event_model(self):
        """Test a new pet is in database"""

        pet = mixer.blend(Event, pet_name='Felix')
        assert pet.pet_name == 'Felix'
        assert Event.objects.filter(pet_name='Felix').exists() is True
