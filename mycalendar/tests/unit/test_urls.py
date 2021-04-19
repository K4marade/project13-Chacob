from django.urls import reverse, resolve


class TestUrls:
    """Class thats tests home urls"""

    def test_mycalendar_url(self):
        """Tests home url"""

        path = reverse('mycalendar')
        assert resolve(path).view_name == 'mycalendar'