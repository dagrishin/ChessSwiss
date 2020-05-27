# Generated by Django 3.0.6 on 2020-05-10 20:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chess_room', '0006_auto_20200511_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='closing_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 20, 59, 26, 856391, tzinfo=utc), verbose_name='Дата закрытия регистрации'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='closing_time',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 20, 59, 26, 856391, tzinfo=utc), verbose_name='Время закрытия регистрации'),
        ),
    ]