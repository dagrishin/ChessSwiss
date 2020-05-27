# Generated by Django 3.0.6 on 2020-05-11 05:46

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chess_room', '0007_auto_20200511_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='closing_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 11, 5, 46, 18, 693852, tzinfo=utc), verbose_name='Дата закрытия регистрации'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='closing_time',
            field=models.TimeField(default=datetime.datetime(2020, 5, 11, 5, 46, 18, 694853, tzinfo=utc), verbose_name='Время закрытия регистрации'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
    ]
