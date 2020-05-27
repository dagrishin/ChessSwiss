# Generated by Django 3.0.6 on 2020-05-10 20:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chess_room', '0004_auto_20200511_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to=settings.AUTH_USER_MODEL, verbose_name='Организатор'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='closing_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 20, 19, 43, 605461, tzinfo=utc), verbose_name='Дата закрытия регистрации'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='closing_time',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 20, 19, 43, 605461, tzinfo=utc), verbose_name='Время закрытия регистрации'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='chess_room.Tournament'),
        ),
    ]