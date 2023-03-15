from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Profile, CustomUser
from .widgets import PictureWidget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname', 'shortname', 'status', 'avatar')
        widgets = {
            'status': forms.Textarea(attrs={'class': 'fixed'}),
            'avatar': PictureWidget()
        }
