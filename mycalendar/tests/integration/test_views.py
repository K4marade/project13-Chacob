from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from mycalendar.models import Event


class TestViews(TestCase):
    """Class that tests mycalendar views"""

    def setUp(self) -> None:
        """Method that sets tests parameters"""

        self.user = get_user_model()
        self.c = Client()

    def test_events_view(self):
        self.user.objects.create_user(username="Leonard",
                                      password="12345Testing")

        self.c.login(username="Leonard", password="12345Testing")

        mycal_url = reverse('mycalendar')
        assert self.c.get(mycal_url).status_code == 200

        response = self.c.post(mycal_url, {
            "date": "20/08/2021 20:00",
            "pet_name": "Felix",
            "reason": "Vaccin",
            "comment": "Test example"
        })

        assert Event.objects.count() == 1
        assert response.status_code == 200

        message = list(response.context['messages'])
        assert len(message) == 1
        assert str(message[0]) == "Votre nouveau rendez-vous a bien été enregistré"
