from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean(self) -> dict:
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def clean(self) -> dict:
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password.')

        return cleaned_data
