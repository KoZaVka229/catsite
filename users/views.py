from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from users.forms import ProfileForm, CustomUserCreationForm
from users.mixins import ProfileRequiredMixin, NoProfileRequiredMixin
from .models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"
    extra_context = {"title": "Регистрация"}


class SignInView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/signin.html"
    extra_context = {"title": "Вход"}


class CreateProfile(LoginRequiredMixin, NoProfileRequiredMixin, CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy("my_profile")
    template_name = "users/profile_create.html"
    extra_context = {"title": "Создание профиля"}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfile(LoginRequiredMixin, ProfileRequiredMixin, UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy("my_profile")
    template_name = "users/profile_edit.html"
    extra_context = {"title": "Обновление профиля"}

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)


class ProfileView(LoginRequiredMixin, ProfileRequiredMixin, DetailView):
    model = Profile
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile'
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        if pk := self.kwargs.get(self.pk_url_kwarg, 0):
            return get_object_or_404(Profile, pk=pk)
        else:
            return get_object_or_404(Profile, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.nickname
        pk = self.kwargs.get(self.pk_url_kwarg, 0)
        context['is_my_profile'] = pk == 0 or pk == self.object.pk

        return context
