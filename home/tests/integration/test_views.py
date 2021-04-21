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
        assert self.c.get(home_url).status_code == 200

        response = self.c.post(home_url, {"search-address": "Paris"})
        assert response.status_code == 200
        # assert response.url == reverse('home')

        response_with_wrong_input = self.c.post(home_url, {"search-address": "!zadkn@@&#="})
        message = list(response_with_wrong_input.context['messages'])
        assert len(message) == 1
        assert str(message[0]) == "Nous n'avons pas pu trouver de résultat. Réessayez"
        assert response_with_wrong_input.status_code == 200

    def test_legal_view(self):
        """Tests the legal view"""

        legal_url = reverse('legal')
        response = self.c.get(legal_url)

        assert response.status_code == 200
