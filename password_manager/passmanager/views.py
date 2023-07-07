from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm

# from django.http import HttpResponse

# Create your views here


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.data)
            return HttpResponseRedirect("/manager")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, "passmanager/index.html", {"form": form})


def manager(request):
    return render(request, "passmanager/manager.html")


def sign_in(request):
    return render(request, "passmanager/signin.html")
