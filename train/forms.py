from dataclasses import fields
from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from train.models import Account, Ticket, Train, TICKET_TRAIN_TYPE_CHOICES, TICKET_CLASS_TYPE_CHOICES, TICKET_PAYMENT_TYPE_CHOICES, TICKET_TYPE_CHOICES, STATION_CHOICES


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


class TicketBookingForm(forms.ModelForm):
    ticket_source = forms.ChoiceField(label='Ticket Source', widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'yourName', 'name': 'name'}), choices=STATION_CHOICES)
    ticket_destination = forms.ChoiceField(label='Ticket Destination', widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'yourName', 'name': 'name'}), choices=STATION_CHOICES)
    ticket_type = forms.ChoiceField(
        label='Ticket Type', widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'tickettype1',
            'name': 'inlineRadioOptions1'
        }), choices=TICKET_TYPE_CHOICES)
    ticket_class = forms.ChoiceField(
        label='Ticket Class', widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'tickettype1',
            'name': 'inlineRadioOptions1'
        }), choices=TICKET_CLASS_TYPE_CHOICES)
    ticket_train = forms.ChoiceField(
        label='Ticket Train', widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'tickettype1',
            'name': 'inlineRadioOptions1'
        }), choices=TICKET_TRAIN_TYPE_CHOICES)
    ticket_payment = forms.ChoiceField(
        label='Ticket Payment', widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'tickettype1',
            'name': 'inlineRadioOptions1'
        }), choices=TICKET_PAYMENT_TYPE_CHOICES)

    class Meta:
        model = Ticket
        fields = [
            'ticket_source', 'ticket_destination', 'ticket_type', 'ticket_class', 'ticket_train', 'ticket_payment'
        ]
        

class CheckFareForm(forms.Form):
    ticket_source = forms.ChoiceField(label='Ticket Source', widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'yourName', 'name': 'name'}), choices=STATION_CHOICES)
    ticket_destination = forms.ChoiceField(label='Ticket Destination', widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'yourName', 'name': 'name'}), choices=STATION_CHOICES)

    class Meta:
        fields = ['ticket_source', 'ticket_destination']