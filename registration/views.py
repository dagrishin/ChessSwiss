from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserRegisterForm
from .models import User


class Login(SuccessMessageMixin, LoginView):
    success_message = _("Вошли в систему")


class Logout(LoginRequiredMixin, LogoutView):
    success_message = _("Вы вышли из системы")

    def get_next_page(self):
        next_page = super().get_next_page()
        if next_page:
            messages.success(self.request, self.success_message)
        return next_page


class AccountCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("auth:login")
    success_message = "Вы успешно зарегестрировались"
