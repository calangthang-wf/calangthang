from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class loginForm(forms.Form):
    lgUsername = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs= {
                'class': 'login_username',
                'name': 'login_username',
                'placeholder': 'Username',
                'type': 'username',
        })
    )

    lgPassword = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.PasswordInput(attrs={
                'class': 'login_password',
                'name': 'login_password',
                'placeholder': 'Password',
                'type': 'password',
        })
    )

    class Meta:
        fields = [
            'lgUsername',
            'lgPassword'
        ]

class registerForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Retype Password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']