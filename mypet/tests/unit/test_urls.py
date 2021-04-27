from django.urls import reverse, resolve


class TestUrls:
    """Class thats tests mycalendar urls"""

    def test_my_pet_url(self):
        """Tests my_pet url"""

        path = reverse('my_pet')
        assert resolve(path).view_name == 'my_pet'
