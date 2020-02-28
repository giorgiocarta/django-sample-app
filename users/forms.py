from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    Add email to the standard registration form
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        This define what model will be affected - i.e. the model
        Also define how to display the form
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    Update username and email
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Update profile picture
    """

    class Meta:
        model = Profile
        fields = ['image']
