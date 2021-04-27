from mixer.backend.django import mixer
import pytest
from mypet.models import Pet


@pytest.mark.django_db
class TestModels:
    """Class that tests mypet models"""

    def test_pet_model(self):
        """Test a new pet is in database"""

        new_pet = mixer.blend(Pet, name='Felix')
        assert new_pet.name == 'Felix'
        assert Pet.objects.filter(name='Felix').exists() is True
        assert Pet.objects.count() == 1
