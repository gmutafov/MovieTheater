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
    # success_url = reverse_lazy('success')

    # def form_valid(self, form):
    #     try:
    #         user = form.save()
    #         login(self.request, user)
    #         return redirect(self.success_url)
    #     # except Exception as e:
    #     #     return redirect('failure')

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    context_object_name = 'login'

    def form_invalid(self, form):
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