from poplib import CR
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.

def index(request):
    return render(request, 'index.html')
     
def login(request):
    return render(request, 'login.html')

def register(request):
    form = CreateUserForm()
    context = {
        'form' : form
    }
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            return redirect('index')
    return render(request, 'register.html', context)

def profile(request):
    return render(request, 'users-profile.html')

def schedule(request):
    return render(request, 'schedule.html')

def quickroutes(request):
    return render(request, 'quickroutes.html')