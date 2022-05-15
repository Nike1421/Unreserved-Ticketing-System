from cgitb import text
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'type':'password', 'align':'center', 'id': 'form3Example4'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'type':'password', 'align':'center', 'id': 'form3Example4'}),
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'id': 'form3Example3'
                }
            )
        }


