import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Ticket, Account

from .forms import RegisterUserForm, UserAuthenticationForm, TicketBookingForm


# Create your views here.

def index(request):
    return render(request, 'train/index.html')
     
def loginUser(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"You are now logged in as {username}.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            print(form.errors)
            messages.error(request, "Invalid Username or Password")
    form = UserAuthenticationForm()
    return render(request, 'train/login.html', {"form": form})

def logoutUser(request):
    logout(request)
    print("You have successfully logged out")
    return redirect('profile')

def registerUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'train/register.html', {'form': form})
    else:
        form = RegisterUserForm()
        return render(request, 'train/register.html', {'form': form})


def profile(request):
    return render(request, 'train/users-profile.html')

def schedule(request):
    return render(request, 'train/schedule.html')

def quickroutes(request):
    return render(request, 'train/quickroutes.html')

def bookticket(request):
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            ticket_source = form.cleaned_data.get('ticket_source')
            ticket_destination = form.cleaned_data.get('ticket_destination')
            ticket_type = form.cleaned_data.get('ticket_type')
            ticket_class = form.cleaned_data.get('ticket_class')
            ticket_train = form.cleaned_data.get('ticket_train')
            ticket_payment = form.cleaned_data.get('ticket_payment')

            new_ticket = {
                'ticket_source' : ticket_source,
                'ticket_destination' : ticket_destination,
                'ticket_type' : ticket_type,
                'ticket_class' : ticket_class,
                'ticket_train' : ticket_train,
                'ticket_payment' : ticket_payment,
                'ticket_holder' : request.user
            }
            
            # print(ticket_source + ticket_destination + ticket_type + ticket_class + ticket_payment + ticket_train)


            messages.success(request, f"Ticket is Successfully Booked")
            return render(request, 'payment', {'ticket': new_ticket})
            # return redirect('profile')
        else:
            messages.error(request, f"Form Error")
    form = TicketBookingForm()
    return render(request, 'train/bookticket.html', {'form': form})

def book():
    pass

def payment(request):
    return render(request, 'train/payment.html')

def fare(request):
    return render(request, 'train/fare.html')

def otp(request):
    return render(request, 'train/otp.html')

def ticket(request):
    return render(request, 'train/ticket.html')

def bookedticket(request):
    return render(request, 'train/bookedticket.html')