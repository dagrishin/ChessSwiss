import os
from django.urls import path, reverse_lazy
from django.contrib.auth import views
# from registrations.forms import UserActivationForm
from chess_room.views import TournamentAllView, TournamentAdd, TournamentDetailView, AddUserTournament, DelUserTournament

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [

    path('', TournamentAllView.as_view(), name='all'),
    path('add/', TournamentAdd.as_view(), name='add'),
    path('turnir-room/<int:pk>/', TournamentDetailView.as_view(), name='detail'),
    path('<int:pk>/add-user/', AddUserTournament.as_view(), name='add-user'),
    path('<int:pk>/del-user/', DelUserTournament.as_view(), name='del-user'),

]