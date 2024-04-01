import pytest
from rest_framework.test import APITestCase

pytestmark = [pytest.mark.django_db]


class TestGuestEndpoint(APITestCase):

    def test_something(self):
        assert True == True