from django.db import models


class Furniture(models.Model):
    name = models.CharField('Название', max_length=25)
    created_at = models.DateField('Дата создания', auto_now_add=True)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'

    def __str__(self):
        return self.name


class Client(models.Model):
    PRIVILEGE = {
        "VIP": "VIP",
        "AVG": "Average",
        "MIN": "Minimun",
    }

    firstname = models.CharField('Имя', max_length=25)
    lastname = models.CharField('Фамилия', max_length=25)
    credit_number = models.IntegerField()
    privilege = models.CharField(max_length=3, choices=PRIVILEGE)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.privilege})"


