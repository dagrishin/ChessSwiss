from django.contrib import admin

from chess_room.models import Tournament, TournamentResult, Player

admin.site.register(Tournament)
admin.site.register(TournamentResult)
admin.site.register(Player)
