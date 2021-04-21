from django.urls import reverse, resolve


class TestUrls:
    """Class thats tests mycalendar urls"""

    def test_mycalendar_url(self):
        """Tests mycalendar url"""

        path = reverse('mycalendar')
        assert resolve(path).view_name == 'mycalendar'
