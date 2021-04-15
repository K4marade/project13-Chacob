from django.urls import reverse, resolve


class TestUrls:
    """Class thats tests home urls"""

    def test_home_url(self):
        """Tests home url"""

        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_legal_url(self):
        """ Tests legal url"""

        path = reverse('legal')
        assert resolve(path).view_name == 'legal'
