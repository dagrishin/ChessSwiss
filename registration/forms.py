from django import forms
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self, commit=True, **kwargs):
        user = self.instance
        if not user.id:
            user.active = True
            user = super(UserRegisterForm, self).save()
        return user