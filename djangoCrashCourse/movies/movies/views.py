from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def movies(request):

    data = Movie.objects.all

    return render(request, 'movies/movies.html', {"movies": data})


def home(response):
    return HttpResponse("home page")



## 45 min