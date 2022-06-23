from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'work_title',
            'professional_summary',
            'skills',
            'linkedin',
            'github',
            'twitter',
            'medium',
            'portfolio'
        ]