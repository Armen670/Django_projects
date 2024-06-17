from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
def index(request): #HttpRequest
    return render(request, "index.html")
    #return HttpResponse("Page about all you can imagane",headers={'secret_code': 213918230912})

def cars(request): #HttpRequest
    return HttpResponse("Page about all cars")

def categories(request, car_id):
    return HttpResponse(f"<h1>Статья о машине под номером </h1><p>{car_id}<p>")
def archive(request,year):
    if year > 2024 or year < 1900:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам  </h1><p>{year}<p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")