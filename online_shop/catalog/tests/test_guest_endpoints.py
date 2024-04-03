import pytest
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from catalog.conftest import EVERYTHING_EQUALS_NOT_NONE

pytestmark = [pytest.mark.django_db]


class TestGuestEndpoints(APITestCase):
    fixtures = ['catalog/tests/fixtures/categories_fixture.json']

    def test_categories_list_endpoints(self):
        url = reverse('categories')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "Мебель, гарнитура и все прилогающее"
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "От трусов с бабочкой до головного убора нормального"
            },
            {
                "id": 3,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "Вся самая модная и лучшая одежда для прерасных дам"
            },
            {
                "id": 4,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "Все для твоих любых домашних животных"
            }
        ]
