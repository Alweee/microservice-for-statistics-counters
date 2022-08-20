from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from api.models import Statistics


class StatisticsApiTests(APITestCase):
    """Класс тестирования Api."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_obj = Statistics.objects.create(
            id='1',
            date='2020-01-01',
            views=54,
            clicks=27,
            cost=17,
        )

    def setUp(self):
        self.data = {
            'id': 2,
            'date': '2020-01-02',
            'views': 60,
            'clicks': 15,
            'cost': 13.4,
        }

    def test_statistics_create(self):
        """Метод создания статистики."""
        cpc = round((self.data.get('cost')) / (self.data.get('clicks')), 2)
        cpm = round((self.data.get('cost')) / (self.data.get('views'))*1000, 2)
        response = self.client.post(reverse('stat-list'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Statistics.objects.count(), 2)
        self.assertEqual(response.json().get('cpc'), cpc)
        self.assertEqual(response.json().get('cpm'), cpm)

    def test_statistics_list(self):
        """Получение списка статистики."""
        response = self.client.get(reverse('stat-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_statistics_retrieve(self):
        """Получение одной записи статистики."""
        response = self.client.get(reverse('stat-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('date'),
                         StatisticsApiTests.test_obj.date)

    def test_statistics_delete(self):
        """Метод удаления статистики."""
        response = self.client.delete(reverse('stat-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Statistics.objects.filter(id=1)), 0)
