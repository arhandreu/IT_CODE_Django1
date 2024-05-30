from django.db import models
from django.urls import reverse

from services.utils import unique_slugify


class Furniture(models.Model):
    objects = models.Manager()
    name = models.CharField('Название', max_length=25)
    created_at = models.DateField('Дата создания', auto_now_add=True)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 blank=True, null=True)
    image = models.ImageField('Фотография мебели',
                              upload_to='photos/%Y/%m/%d/',
                              blank=True, null=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, blank=True)

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('furniture', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)


class Client(models.Model):
    PRIVILEGE = {
        "MIN": "Minimum",
        "AVG": "Average",
        "VIP": "VIP",
    }

    objects = models.Manager()
    firstname = models.CharField('Имя', max_length=25)
    lastname = models.CharField('Фамилия', max_length=25)
    credit_number = models.IntegerField()
    privilege = models.CharField(max_length=3, choices=PRIVILEGE, default=PRIVILEGE["MIN"])
    orders = models.ManyToManyField(Furniture, through='Order', related_name='orders_client', blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.privilege})"


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField('Название категории', max_length=100,
                            db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]


class Order(models.Model):

    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, verbose_name="Мебель", on_delete=models.CASCADE)
    number_order = models.PositiveIntegerField(verbose_name="Номер заказа")
    date_order = models.DateField(auto_now_add=True, verbose_name="Дата заказа")
    date_delivery = models.DateField(verbose_name="Дата доставки")
    status = models.BooleanField(default=False, verbose_name="Статус доставки")
    count = models.PositiveIntegerField(verbose_name="Количество", default=0)

    def __str__(self):
        return f"{self.client} + {self.furniture}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['date_delivery', 'number_order']


class NavBar(models.Model):
    objects = models.Manager()
    name = models.CharField('Название', max_length=25)
    url = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

