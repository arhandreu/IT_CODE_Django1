import datetime

from django.test import TestCase, Client
from homew import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category_chair = models.Category.objects.create(
            name='Стулья',
        )
        self.category_table = models.Category.objects.create(
            name='Столы'
        )
        self.furniture = models.Furniture.objects.create(
            name='Стул',
            created_at=datetime.datetime.now(),
            price=150,
            category=self.category_chair,
        )

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_magazine(self):
        response = self.client.get('/magazine/')
        self.assertEqual(response.status_code, 302)

    def test_category(self):
        response = self.client.get(f'/category/{self.furniture.category.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/index/')
        self.assertNotEqual(response.status_code, 400)
