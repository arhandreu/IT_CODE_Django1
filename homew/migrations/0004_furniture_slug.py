# Generated by Django 5.0.4 on 2024-05-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homew', '0003_furniture_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
