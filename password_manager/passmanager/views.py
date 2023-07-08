from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from django import forms

# from django.http import HttpResponse

# Create your views here


def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = form.data.get('user')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            if user: 
                login(request, user=user)
                return HttpResponseRedirect("/manager")
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "passmanager/index.html")

    return render(request, "passmanager/index.html")

@login_required()
def manager(request):
    return render(request, "passmanager/manager.html")


def sign_up(request):
    if request.method =="POST":
        pass
    return render(request, "passmanager/signup.html")


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")
