from mixer.backend.django import mixer
import pytest
from mycalendar.models import Event


@pytest.mark.django_db
class TestModels:
    """Class that tests mycalendar models"""

    def test_event_model(self):
        """Test a new event is in database"""

        event_reason = mixer.blend(Event, reason='Vaccin')
        assert event_reason.reason == 'Vaccin'
        assert Event.objects.filter(reason='Vaccin').exists() is True
        assert Event.objects.count() == 1
