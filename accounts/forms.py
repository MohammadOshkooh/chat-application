from allauth.account.forms import LoginForm, SignupForm
from django import forms

from .models import Profile


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'input100'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input100'})


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input100'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'input100'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input100'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input100'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
