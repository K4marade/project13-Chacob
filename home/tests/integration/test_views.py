from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Class that tests home views"""

    def setUp(self) -> None:
        """Method that sets tests parameters"""

        self.c = Client()

    def test_home_view(self):
        """Tests the home view"""

        home_url = reverse('home')
        response = self.c.get(home_url)

        assert response.status_code == 200

    def test_legal_view(self):
        """Tests the legal view"""

        legal_url = reverse('legal')
        response = self.c.get(legal_url)

        assert response.status_code == 200
