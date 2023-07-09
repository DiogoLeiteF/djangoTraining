from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import MD5PasswordHasher
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from .models import PasswordsList


# from django.http import HttpResponse

# Create your views here


def index(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user=user)
            return HttpResponseRedirect("/manager")
    # if a GET (or any other method) we'll create a blank form
    return render(request, "passmanager/index.html")


@login_required()
def manager(request):
    data = {}
    user = request.user
    pass_list = PasswordsList.objects.filter(user=user)
    data["list"] = pass_list
    data["user"] = user.username
    return render(request, "passmanager/manager.html", context=data)


def sign_up(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("user")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if username and email and password1 and password2:
            if password2 == password1:
                user_qs = User.objects.filter(username=username)
                email_qs = User.objects.filter(email=email)

                if user_qs.exists() or email_qs.exists():
                    data = {"msg": "user already exists"}
                else:
                    newuser = User(username=username, email=email)
                    newuser.set_password(password1)
                    newuser.save()
                    login(request, user=newuser)
                    return HttpResponseRedirect("/manager")

    return render(request, "passmanager/signup.html", context=data)


def edit_data(request):
    if request.method == "POST":
        _id = request.POST.get("id")
        site = request.POST.get("site")
        password = request.POST.get("password")
        notes = request.POST.get("notes")
        edit = PasswordsList.objects.filter(id=_id).first()
        if edit:
            edit.site = site
            edit.password = password
            edit.notes = notes
            edit.save()
        return redirect("/manager")


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")
