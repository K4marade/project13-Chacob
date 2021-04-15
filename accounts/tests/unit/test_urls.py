from django.urls import reverse, resolve


class TestUrls:
    """Class that tests account urls"""

    def test_login_url(self):
        """Tests login url"""

        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_register_url(self):
        """Tests register url"""

        path = reverse('register')
        assert resolve(path).view_name == 'register'

    def test_logout_url(self):
        """Tests logout url"""

        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

    def test_profile_url(self):
        """Tests profile url"""

        path = reverse('profile')
        assert resolve(path).view_name == 'profile'

    def test_password_reset_url(self):
        """Tests password reset url"""

        path = reverse('password_reset')
        assert resolve(path).view_name == 'password_reset'

    def test_password_sent_url(self):
        """Tests password reset url"""

        path = reverse('password_reset_done')
        assert resolve(path).view_name == 'password_reset_done'

    # def test_password_confirm_url(self):
    #     """Tests password confirm url"""
    #
    #     path = reverse('password_reset_confirm')
    #     assert resolve(path).view_name == 'password_reset_confirm'

    def test_password_complete_url(self):
        """Tests password complete url"""

        path = reverse('password_reset_complete')
        assert resolve(path).view_name == 'password_reset_complete'

    def test_password_change_url(self):
        """Tests password change url"""

        path = reverse('password_change')
        assert resolve(path).view_name == 'password_change'

    def test_password_change_done_url(self):
        """Tests password change done url"""

        path = reverse('password_change_done')
        assert resolve(path).view_name == 'password_change_done'
