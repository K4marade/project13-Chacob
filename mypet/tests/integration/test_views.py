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

    def tests_create_pet_view(self):
        """Tests create pet view"""

        # Create and log a new user
        self.user.objects.create_user(username="Leonard",
                                      password="12345Testing")
        self.c.login(username="Leonard", password="12345Testing")

        new_pet_url = reverse('mypet')
        assert self.c.get(new_pet_url).status_code == 200

        response = self.c.post(new_pet_url, {
            "species": "cat",
            "gender": "male",
            "birth_date": "23/04/2021",
            "name": "Felix"
        }, follow=True)

        assert response.status_code == 200

        # Assert a new pet is created
        assert Pet.objects.count() == 1

        pet_name = Pet.objects.get(name="Felix").name

        # Assert a confirmation message is displayed on the page
        message = list(response.context['messages'])
        assert len(message) == 1
        assert str(message[0]) == pet_name + " a bien été ajouté !"

    def test_update_pet_view(self):
        """Tests update pet view"""

        # Create and log a new user
        user = self.user.objects.create_user(username="Leonard",
                                             password="12345Testing")
        self.c.login(username="Leonard", password="12345Testing")

        # Create a new pet
        pet = Pet.objects.create(id=1,
                                 user_id=user.id,
                                 species="cat",
                                 gender="male",
                                 birth_date="2021-04-23",
                                 name="Felix")

        # Assert new pet is in the database
        assert Pet.objects.count() == 1
        assert pet.name == "Felix"

        new_pet = Pet.objects.get(id=pet.id)

        update_url = reverse("update_my_pet", kwargs={"id_pet": new_pet.id})
        assert self.c.get(update_url).status_code == 200

        response = self.c.post(update_url, {"species": "cat",
                                            "gender": "male",
                                            "birth_date": "23/04/2021",
                                            "name": "New Felix"}, follow=True)
        assert response.status_code == 200

        modified_pet = Pet.objects.get(id=pet.id)

        # Assert new pet is the same one than modified pet
        assert modified_pet.id == new_pet.id

        # Assert the name has been modified
        assert modified_pet.name != new_pet.name

    def test_delete_pet_view(self):
        """Test delete pet view"""

        # Create and log a new user
        user = self.user.objects.create_user(username="Leonard",
                                             password="12345Testing")
        self.c.login(username="Leonard", password="12345Testing")

        # Create a new pet
        pet = Pet.objects.create(user_id=user.id,
                                 species="cat",
                                 gender="male",
                                 birth_date="2021-04-23",
                                 name="Felix")

        # Assert one pet is in the database
        assert Pet.objects.count() == 1

        pet_id = Pet.objects.get(id=pet.id).id

        delete_url = reverse("delete_my_pet", kwargs={"id_pet": pet_id})
        response = self.c.get(delete_url)

        # Assert user is redirected to mypet page
        assert response.status_code == 302

        # Assert no pets are in the database
        assert Pet.objects.count() == 0
