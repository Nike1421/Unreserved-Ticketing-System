from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from train.models import Account


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'id': 'yourPassword'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'id': 'yourPassword2'}),
    )

    class Meta:
        model = Account
        fields = ['username', 'name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'yourUsername'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'yourName'
                }
            )
        }

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Mobile Number",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'yourUsername',
                'type': 'text'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'id': 'yourPassword'}),
    )

    class Meta:
        model = Account
        fields = ['username',  'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'yourUsername'
                }
            ),
            
        }