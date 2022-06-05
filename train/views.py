from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, UserAuthenticationForm, TicketBookingForm, CheckFareForm
from .models import Ticket
from django.template.defaulttags import register
# Create your views here.

booked_ticket = {}
@login_required(login_url='login', redirect_field_name='index')
def index(request):
    tickets = Ticket.objects.all().filter(ticket_user = request.user)
    return render(request, 'train/index.html', {'tickets': tickets})
     
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
            messages.error(request, "Invalid Username or Password")
    form = UserAuthenticationForm()
    return render(request, 'train/login.html', {"form": form})

@login_required(login_url='login')
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

@login_required(login_url='login', redirect_field_name='profile')
def profile(request):
    return render(request, 'train/users-profile.html')

def schedule(request):
    return render(request, 'train/schedule.html')

def quickroutes(request):
    return render(request, 'train/quickroutes.html')

@login_required(login_url='login', redirect_field_name='bookticket')
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
                "ticket_source" : ticket_source,
                "ticket_destination" : ticket_destination,
                "ticket_type" : ticket_type,
                "ticket_class" : ticket_class,
                "ticket_train" : ticket_train,
                "ticket_payment" : ticket_payment,
                "ticket_holder" : request.user.name,
                "ticket_time" : date.today()
            }
            if ticket_source == 'None':
                messages.error(request, 'Please enter the source of your trip')
            elif ticket_destination == 'None':
                messages.error(request, 'Please enter the destination of your trip')
            elif ticket_destination == ticket_source:
                messages.error(request, 'Source and Destination cannot be the same!')
            else:
                global booked_ticket
                booked_ticket = new_ticket
                return render(request, 'train/payment.html')
        else:
            messages.error(request, f"Form Error")
    form = TicketBookingForm()
    return render(request, 'train/bookticket.html', {'form': form})

def book():
    pass

@login_required(login_url='login', redirect_field_name='payment')
def payment(request):
    if request.method == "POST":
        return render(request, 'train/bookedticket.html')
    return render(request, 'train/payment.html')

def fare(request):
    form = CheckFareForm()
    return render(request, 'train/fare.html', {'form': form})

def otp(request):
    return render(request, 'train/otp.html')

def blank(request):
    return render(request, 'train/blank.html')

@login_required(login_url='login')
def bookedticket(request):
    global booked_ticket
    new_ticket = Ticket.objects.create(
        ticket_source = booked_ticket['ticket_source'],
        ticket_destination = booked_ticket['ticket_destination'],
        ticket_type = booked_ticket['ticket_type'],
        ticket_class = booked_ticket['ticket_class'],
        ticket_train = booked_ticket['ticket_train'],
        ticket_payment = booked_ticket['ticket_payment'],
        ticket_fare = 20,
        ticket_user = request.user,
    )
    print(booked_ticket)
    return render(request, 'train/bookedticket.html', {'ticket': booked_ticket})

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)