from django import forms
from .models import Profile, Storyboard, CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'background_color']

class StoryboardForm(forms.ModelForm):
    class Meta:
        model = Storyboard
        fields = ['text', 'photo', 'video']