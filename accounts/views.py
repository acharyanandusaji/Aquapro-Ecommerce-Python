from django.shortcuts import render, redirect
from .forms import UserCreationForm, SignUpForm
from shop import views, urls
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hm")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect("hm")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
