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


class TestClientAPI(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_client_1 = models.Client.objects.create(
            firstname='Александр',
            lastname='Кошевой',
            credit_number=65465468,
            privilege='AVG'
        )
        self.api_client_2 = models.Client.objects.create(
            firstname='Евгений',
            lastname='Тютчев',
            credit_number=68468468,
            privilege='MIN'
        )

    def test_create(self):
        data_client = {'firstname': 'Николай',
                       'lastname': 'Пупыркин',
                       'credit_number': 9849849,
                       'privilege': 'VIP',
                       }

        response = self.client.post('/clientMV/', data=data_client)
        self.assertEqual(response.status_code, 201)

    def test_list(self):
        response = self.client.get('/clientMV/')
        self.assertEqual(len(response.data), 2)

    def test_detail(self):
        response = self.client.get(f'/clientMV/{self.api_client_2.pk}/')
        self.assertEqual(response.data['privilege'], 'MIN')

    def test_update(self):
        data_client = {'firstname': 'Василий',
                       'lastname': 'Морозов',
                       'credit_number': 898484846,
                       'privilege': 'AVG',
                       }
        self.client.put(f'/clientMV/{self.api_client_1.pk}/',
                        data=data_client,
                        content_type='application/json')
        self.assertDictEqual(models.Client.objects.filter(
            pk=self.api_client_1.pk)
                             .values('firstname', 'lastname',
                                     'credit_number', 'privilege')[0],
                             data_client)

    def test_partial_update(self):
        data_client = {
            'privilege': 'AVG',
        }
        response = self.client.patch(f'/clientMV/{self.api_client_2.pk}/',
                                     data=data_client,
                                     content_type='application/json')

        self.assertEqual(response.data['privilege'], data_client['privilege'])

    def test_delete(self):
        response = self.client.delete(f'/clientMV/{self.api_client_2.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(models.Client.objects.filter(
            pk=self.api_client_2.pk)), 0)
