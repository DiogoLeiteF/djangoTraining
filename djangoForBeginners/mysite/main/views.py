from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<a href='v1/'>link to v1</a>")



def v1(response):
    return HttpResponse("v1 page")

## Todo 
## 22 min part 2