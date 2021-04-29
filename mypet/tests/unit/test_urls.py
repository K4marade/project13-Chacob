from django.urls import reverse, resolve


class TestUrls:
    """Class thats tests mycalendar urls"""

    def test_my_pet_url(self):
        """Tests my_pet url"""

        path = reverse('my_pet')
        assert resolve(path).view_name == 'my_pet'

    def test_update_my_pet_url(self):
        """Tests update_my_pet_url"""

        path = reverse("update_my_pet", kwargs={'id_pet': 1})
        assert resolve(path).view_name == "update_my_pet"

    def test_delete_my_pet_url(self):
        """Tests delete_my_pet_url"""

        path = reverse("delete_my_pet", kwargs={'id_pet': 1})
        assert resolve(path).view_name == "delete_my_pet"
