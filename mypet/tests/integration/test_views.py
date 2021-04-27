from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from mypet.models import Pet


class TestViews(TestCase):
    """Class that tests mycalendar views"""

    def setUp(self) -> None:
        """Method that sets tests parameters"""

        self.user = get_user_model()
        self.c = Client()

    def tests_my_pet_view(self):
        self.user.objects.create_user(username="Leonard",
                                      password="12345Testing")

        self.c.login(username="Leonard", password="12345Testing")

        new_pet_url = reverse('my_pet')
        assert self.c.get(new_pet_url).status_code == 200

        response = self.c.post(new_pet_url, {
            "species": "cat",
            "gender": "male",
            "birth_date": "23/04/2021",
            "name": "Felix"
        }, follow=True)
        assert response.status_code == 200

        assert Pet.objects.count() == 1

        pet_name = Pet.objects.get(name="Felix").name

        message = list(response.context['messages'])
        assert len(message) == 1
        assert str(message[0]) == pet_name + " a bien été ajouté !"
