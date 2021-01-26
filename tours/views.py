from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from random import randint

from django.db.models import Max, Min
from .models import Tours, Depart


def MainView(request):
    tours = Tours.objects.all()
    random_tours = []
    while len(random_tours) != 6:
        random = randint(0, len(tours) - 1)
        if tours[random] not in random_tours:
            random_tours.append(tours[random])
    return render(request, 'tours/index.html', {'random_tours': random_tours})


def DepartureView(request, departure):
    tours = Tours.objects.select_related("departure").filter(departure__title=departure)
    max_min_price = tours.aggregate(Max('price'), Min('price'), Max('nights'), Min('nights'))
    departure_ru = Depart.objects.get(title=departure).ru_departure
    return render(request, 'tours/departure.html',
                  {'tours': tours, 'departure_ru': departure_ru, 'max_min_price': max_min_price})


def TourView(request, id):
    tour = Tours.objects.select_related("departure").get(id=id)
    departure_ru = tour.departure.ru_departure
    return render(request, 'tours/tour.html', {'tour': tour, 'departure_ru': departure_ru})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def ServerError(request):
    return HttpResponseServerError('<h1>Извините, произошел '
                                   'внутрисистемный сбой</h1>')
