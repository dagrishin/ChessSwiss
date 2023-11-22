from django import forms

from chess_room.models import Tournament


class MyDateInput(forms.DateInput):
    input_type = "date"


class MyTimeInput(forms.TimeInput):
    input_type = "time"


class CreateTournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        exclude = ["author", "players", "is_open"]
        widgets = {
            "closing_date": MyDateInput(),
            "closing_time": MyTimeInput(),
        }
