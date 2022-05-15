from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

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