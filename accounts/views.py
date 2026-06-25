from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import AppUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('movie-list')

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
        storage = messages.get_messages(self.request)
        storage.used = True

        messages.error(self.request, "The username or password is incorrect.")
        return super().form_invalid(form)

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = AppUser
    form_class = CustomUserChangeForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDeleteView(DeleteView):
    model = AppUser
    template_name = 'profile/profile-delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('success')

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        logout(request)
        return HttpResponseRedirect(self.success_url)