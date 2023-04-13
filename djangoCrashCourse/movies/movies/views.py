from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Movie


def movies(request):

    data = Movie.objects.all

    return render(request, 'movies/movies.html', {"movies": data})


def home(response):
    return HttpResponse("home page")


def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {"movie": data})


def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        print(title, year)

        if title and year:
            movie = Movie(title=title, year=year)
            movie.save()
            return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')


def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    
    movie.delete()
    return HttpResponseRedirect('/movies')




# 45 min
