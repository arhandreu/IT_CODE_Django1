from django.db import models
from django.urls import reverse


class Furniture(models.Model):
    objects = models.Manager()
    name = models.CharField('Название', max_length=25)
    created_at = models.DateField('Дата создания', auto_now_add=True)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория',
                                 blank=True, null=True)
    image = models.ImageField('Фотография мебели', upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'

    def __str__(self):
        return self.name


class Client(models.Model):
    PRIVILEGE = {
        "VIP": "VIP",
        "AVG": "Average",
        "MIN": "Minimum",
    }

    objects = models.Manager()
    firstname = models.CharField('Имя', max_length=25)
    lastname = models.CharField('Фамилия', max_length=25)
    credit_number = models.IntegerField()
    privilege = models.CharField(max_length=3, choices=PRIVILEGE)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.privilege})"


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField('Название категории', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]
