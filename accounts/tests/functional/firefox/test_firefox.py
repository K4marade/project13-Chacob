from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core import mail
import time
import re

firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920,1200")


class FirefoxFunctionalTestCase(StaticLiveServerTestCase):
    """Class that defines Chrome functional tests"""

    def setUp(self):
        """Tests setup method"""

        self.driver = webdriver.Chrome(options=firefox_options, )
        self.driver.maximize_window()
        self.user = get_user_model()

    def tearDown(self):
        """Tests tear down method"""

        self.driver.close()

    def get_element(self, selector):
        """Method that uses a css selector to return
        an element from the driver."""

        return self.driver.find_element_by_css_selector(selector)

    def test_user_can_connect_and_disconnect(self):
        """
        Test user is on the homepage and :
            - clicks on the login button
            - inputs its connexion info and clicks on "connexion" button
            - clicks on the logout button from the homepage and is disconnected
        """

        self.user.objects.create_user(
            username="LeonardCOLIN", password="1234Testing!"
        )

        self.driver.get(self.live_server_url)

        # User is on the homepage and clicks on the login button
        self.get_element("#button-login").click()

        time.sleep(1)

        # Assert the current url is the login url
        assert self.driver.current_url == self.live_server_url + reverse(
            'login') + "?next=/"

        self.get_element("#id_username").send_keys("LeonardCOLIN")
        self.get_element("#id_password").send_keys("1234Testing!")
        self.get_element("#button-connexion").click()

        time.sleep(2)

        # Assert the current url is the home url
        assert self.driver.current_url == self.live_server_url + \
               reverse("home")
        # Assert the profile link is available once user is authenticated
        assert "button-profile" in self.driver.page_source

        # User clicks on the logout button
        self.get_element("#button-logout").click()
        time.sleep(1)
        # Assert user is logged out
        assert "Vous êtes bien déconnecté" in self.driver.page_source

    def test_user_can_register(self):
        """
        Test user is on the homepage and:
            - clicks on the register button
            - inputs its username, email and password
            - clicks on the "validate" button and is now registered
        """

        self.driver.get(self.live_server_url)

        # User is on the homepage and clicks on the register button
        self.get_element("#button-register").click()

        # Assert the current url is the login url
        assert self.driver.current_url == self.live_server_url + reverse(
            'register') + "?next=/"
        time.sleep(2)

        self.get_element("#id_username").send_keys("Leonard")
        self.get_element("#id_email").send_keys("leocolin@leo.com")
        self.get_element("#id_password1").send_keys("testPassword1234")
        self.get_element("#id_password2").send_keys("testPassword1234")
        time.sleep(2)
        self.get_element("#button-validate").click()
        time.sleep(1)
        assert "Bienvenue Leonard" in self.driver.page_source

    def test_user_can_reset_password(self):
        self.user.objects.create_user(
            username="LeonardCOLIN",
            password="1234Testing!",
            email="testing@purbeurre.com"
        )

        self.driver.get(self.live_server_url)

        # User is on the homage and clicks on the login button
        self.get_element("#button-login").click()

        # Assert the current url is the login url
        assert self.driver.current_url == self.live_server_url + reverse(
            'login') + "?next=/"
        time.sleep(2)

        # User clicks on the "forgotten password" button
        self.get_element("#button-reset-password").click()
        time.sleep(1)

        # User puts his email and clicks on the "Send" button
        self.get_element("#id_email").send_keys("testing@purbeurre.com")
        self.get_element("#button-confirm").click()

        # assert one message has been sent
        assert len(mail.outbox) == 1

        # get the unique url from the message
        message = mail.outbox[0].body
        url = re.findall(r'(https?://\S+)', message)
        self.driver.get(url[0])
        time.sleep(1)

        # User puts his new password twice and clicks on the confirm button
        self.get_element("#id_new_password1").send_keys("TestingNewPassword12345")
        self.get_element("#id_new_password2").send_keys("TestingNewPassword12345")
        self.get_element("#button-confirm").click()
        time.sleep(2)

        # User clicks on the login button
        self.get_element("#connexion").click()
        time.sleep(1)

        # User is logging in with his new password
        self.get_element("#id_username").send_keys("LeonardCOLIN")
        self.get_element("#id_password").send_keys("TestingNewPassword12345")
        self.get_element("#button-connexion").click()

    def test_user_can_change_password(self):
        self.user.objects.create_user(
            username="LeonardCOLIN",
            password="1234Testing!",
            email="testing@purbeurre.com"
        )

        self.driver.get(self.live_server_url)

        # User is on the homepage and clicks on the login button
        self.get_element("#button-login").click()
        time.sleep(1)

        self.get_element("#id_username").send_keys("LeonardCOLIN")
        self.get_element("#id_password").send_keys("1234Testing!")
        self.get_element("#button-connexion").click()
        time.sleep(2)

        # User is connected, on the homage and clicks on the account profile button
        self.get_element("#button-profile").click()
        time.sleep(1)

        # User clicks on the change password link
        self.get_element("#button-change-password").click()
        time.sleep(2)

        # User puts his old and new passwords
        self.get_element("#id_old_password").send_keys("1234Testing!")
        self.get_element("#id_new_password1").send_keys("TestingChange1234")
        self.get_element("#id_new_password2").send_keys("TestingChange1234")
        self.get_element("#button-confirm").click()
        time.sleep(2)

        # User clicks on the logout button
        self.get_element("#button-logout").click()
        time.sleep(1)
        self.get_element("#close-cross-button").click()

        # User clicks on the login button
        self.get_element("#button-login").click()
        time.sleep(1)

        # User logs in using his new password
        self.get_element("#id_username").send_keys("LeonardCOLIN")
        self.get_element("#id_password").send_keys("TestingChange1234")
        self.get_element("#button-connexion").click()
        time.sleep(2)

        # Assert the profile link is available once user is authenticated with his new password
        assert "button-profile" in self.driver.page_source
