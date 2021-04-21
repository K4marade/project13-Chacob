from django.core import mail
from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth import get_user_model
import re


class TestViews(TestCase):
    """Class that tests account views"""

    def setUp(self) -> None:
        """Method that sets tests parameters"""

        self.user = get_user_model()
        self.c = Client()

    def test_user_register_view(self):
        """Tests the account register view"""

        # Assert no user is registered yet
        assert self.user.objects.count() == 0

        register_url = reverse('register')
        assert self.c.get(register_url).status_code == 200

        response = self.c.post(register_url, {
            "username": "Leonard",
            "email": "leo@leo.com",
            "password1": "12345Testing",
            "password2": "12345Testing"
        })

        # Assert one user is now registered
        assert self.user.objects.count() == 1

        # Homepage redirection once registered
        assert response.status_code == 302
        assert response.url == reverse('home')

    def test_user_login_view(self):
        """Tests the account login view with success and fail"""

        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")
        assert self.user.objects.count() == 1
        login_url = reverse("login")
        assert self.c.get(login_url).status_code == 200

        # Correct username and password:
        response = self.c.post(login_url, {"username": "Leonard",
                                           "password": "12345Testing"})

        # Homepage redirection once logged in
        assert response.status_code == 302
        assert response.url == reverse("home")

        # Incorrect password:
        response_with_wrong_password = self.c.post(
            login_url, {"username": "Leonard",
                        "password": "wrong_password"}
        )
        assert response_with_wrong_password.status_code == 200
        assert b"Your username and password didn\'t match" in \
               response_with_wrong_password.content

    def test_logout_view(self):
        """Tests the account logout view"""

        logout_url = reverse("logout")
        response = self.c.get(logout_url)

        # Homepage redirection once logged out
        assert response.status_code == 302
        assert response.url == reverse("home")

    def test_profile_view(self):
        """Tests the account profile view"""

        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")

        self.c.login(username="Leonard", password="12345Testing")
        profile_url = reverse("profile")
        response = self.c.get(profile_url)
        assert response.status_code == 200

    def test_reset_password_view(self):
        """tests the reset password view"""

        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")

        reset_password_url = reverse("password_reset")
        assert self.c.get(reset_password_url).status_code == 200

        response_email_sent = self.c.post(reset_password_url, {"email": "leo@leo.com"})

        assert response_email_sent.status_code == 302
        assert response_email_sent.url == reverse("password_reset_done")
        assert len(mail.outbox) == 1

        email_msg = mail.outbox[0].body
        uidb64, token = re.findall(
            r"/([\w\-]+)",
            re.search(r"^http\://.+$", email_msg, flags=re.MULTILINE)[0])[3:5]

        msg_reset_url = reverse("password_reset_confirm", args=(uidb64, token))
        response_reset_url = self.c.get(msg_reset_url, follow=True)
        assert response_reset_url.status_code == 200

        confirm_reset_url = reverse("password_reset_confirm", args=(uidb64, "set-password"))
        response_confirm_reset_password = self.c.post(confirm_reset_url,
                                                      {"new_password1": "TestingReset12345",
                                                       "new_password2": "TestingReset12345"},
                                                      follow=True)

        assert response_confirm_reset_password.status_code == 200
        assert self.c.login(username="Leonard", password="TestingReset12345") is True

    def test_change_password_view(self):
        """tests the change password view"""

        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")

        self.c.login(username="Leonard", password="12345Testing")

        change_password_url = reverse("password_change")
        assert self.c.get(change_password_url).status_code == 200

        response = self.c.post(change_password_url, {"old_password": "12345Testing",
                                                     "new_password1": "Testing12345",
                                                     "new_password2": "Testing12345"})

        assert response.status_code == 302
        assert response.url == reverse("password_change_done")
        assert self.c.login(username="Leonard", password="Testing12345") is True
