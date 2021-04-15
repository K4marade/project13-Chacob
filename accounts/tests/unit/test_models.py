from mixer.backend.django import mixer
import pytest
from accounts.models import UserAuth


@pytest.mark.django_db
class TestModels:
    """Class that tests account models"""

    def test_user_auth(self):
        """Test a new user is in database"""

        user = mixer.blend(UserAuth, username='test user')
        assert user.username == 'test user'
        assert UserAuth.objects.filter(username='test user').exists() is True
