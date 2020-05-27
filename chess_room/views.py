from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.middleware.csrf import CsrfViewMiddleware
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import View

from chess_room.forms import CreateTournamentForm
from chess_room.models import Tournament

class UserAuthMixin(UserPassesTestMixin):
    url_redirect = reverse_lazy('auth:login')

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return HttpResponseRedirect(self.url_redirect)

class UserCreateTournamentMixin(LoginRequiredMixin, UserPassesTestMixin):
    url_redirect = reverse_lazy('auth:login')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponseRedirect(self.url_redirect)


class TournamentAllView(ListView):
    model = Tournament
    template_name = 'chess_room/tournaments.html'


class TournamentAdd(UserCreateTournamentMixin, CreateView):
    model = Tournament
    form_class = CreateTournamentForm
    template_name = 'chess_room/create_tournament.html'
    success_url = reverse_lazy('tournaments:all')


class TournamentDetailView(LoginRequiredMixin, DetailView):
    model = Tournament
    template_name = 'chess_room/detail_tournament.html'


class AddUserTournament(CsrfViewMiddleware, LoginRequiredMixin, View):
    """Класс добавление пользователей в турнир"""

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = 'Вы присоедеинились к турниру'
            user = request.user
            tournament_add = Tournament.objects.get(id=kwargs['pk'])
            tournament_add.players.add(user)
            # try:
            #     pass
            # except IntegrityError as error:
            #     result = error

            return JsonResponse({'result': result})

class DelUserTournament(CsrfViewMiddleware, LoginRequiredMixin, View):
    """Класс удаления пользователей из турнир"""

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = 'Вы покинули турнир'
            user = request.user
            tournament_add = Tournament.objects.get(id=kwargs['pk'])
            tournament_add.players.remove(user)
            # try:
            #     pass
            # except IntegrityError as error:
            #     result = error

            return JsonResponse({'result': result})
