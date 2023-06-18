from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class SignupForm(UserCreationForm):
    """
    A form for user signup.

    Inherits from UserCreationForm, a built-in form for user registration
    with password handling.

    Attributes:
        model (User): The User model to be used for user registration.
        fields (list): The fields to be included in the form.

    """
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating user information.

    Inherits from ModelForm, a generic form for updating model instances.

    Attributes:
        model (User): The User model to be updated.
        fields (list): The fields to be included in the form.

    """
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating user profile information.

    Inherits from ModelForm, a generic form for updating model instances.

    Attributes:
        model (Profile): The Profile model to be updated.
        fields (list): The fields to be included in the form.

    """
    class Meta:
        model = Profile
        fields = [
            'work_title',
            'professional_summary',
            'image',
            'skills',
            'resume',
            'linkedin',
            'github',
            'twitter',
            'portfolio'
        ]
