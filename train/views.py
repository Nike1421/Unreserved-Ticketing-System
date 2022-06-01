import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterUserForm, UserAuthenticationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')
     
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
            print("User Logged In")
            return redirect('profile')
    else:
        form = RegisterUserForm()
        return render(request, 'train/register.html', {'form': form})


def profile(request):
    return render(request, 'users-profile.html')

def schedule(request):
    return render(request, 'schedule.html')

def quickroutes(request):
    return render(request, 'quickroutes.html')

def bookticket(request):
    return render(request, 'bookticket.html')

def payment(request):
    return render(request, 'payment.html')

def fare(request):
    return render(request, 'fare.html')

def otp(request):
    return render(request, 'otp.html')

def ticket(request):
    return render(request, 'ticket.html')