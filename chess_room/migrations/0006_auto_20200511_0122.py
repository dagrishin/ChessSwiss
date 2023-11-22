# Generated by Django 3.0.6 on 2020-05-10 20:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ("chess_room", "0005_auto_20200511_0119"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournament",
            name="closing_date",
            field=models.DateField(
                default=datetime.datetime(2020, 5, 10, 20, 22, 29, 466735, tzinfo=utc),
                verbose_name="Дата закрытия регистрации",
            ),
        ),
        migrations.AlterField(
            model_name="tournament",
            name="closing_time",
            field=models.TimeField(
                default=datetime.datetime(2020, 5, 10, 20, 22, 29, 466735, tzinfo=utc),
                verbose_name="Время закрытия регистрации",
            ),
        ),
        migrations.AlterField(
            model_name="tournament",
            name="tournament",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="parent",
                to="chess_room.Tournament",
            ),
        ),
    ]
