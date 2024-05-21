# Generated by Django 5.0.4 on 2024-04-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25,
                                               verbose_name='Имя')),
                ('lastname', models.CharField(max_length=25,
                                              verbose_name='Фамилия')),
                ('credit_number', models.IntegerField()),
                ('privilege', models.CharField(
                    choices=[('VIP', 'VIP'), ('AVG', 'Average'),
                             ('MIN', 'Minimun')],
                    max_length=3)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=25,
                                          verbose_name='Название')),
                ('created_at', models.DateField(auto_now_add=True,
                                                verbose_name='Дата создания')),
                ('price', models.DecimalField(decimal_places=2,
                                              max_digits=5,
                                              verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Мебель',
                'verbose_name_plural': 'Мебель',
            },
        ),
    ]