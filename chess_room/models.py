from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from registration.models import User


class Tournament(models.Model):
    title = models.CharField(max_length=200)
    tournament = models.ForeignKey('self', related_name='parent', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, verbose_name=_('Организатор'), related_name='organizer', on_delete=models.CASCADE, default=2)
    players = models.ManyToManyField(User, verbose_name=_('Участники'), blank=True, null=True)
    closing_date = models.DateField(verbose_name=_('Дата закрытия регистрации'), default=timezone.now())
    closing_time = models.TimeField(verbose_name=_('Время закрытия регистрации'), default=timezone.now())
    is_open = models.BooleanField(verbose_name=_('Статус регистрации'), default=True)
    number_of_tours = models.IntegerField(verbose_name=_('Количество туров в турнире'))

    def __str__(self):
        return self.title


class Player(models.Model):

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.IntegerField()
    result = models.FloatField()


class TournamentResult(models.Model):

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_user')
    rival = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rival_user')
    result = models.FloatField()
    additional_indicator = models.FloatField()
    tour = models.IntegerField()
