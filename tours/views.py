from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse


def main_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'index.html')


def departure_view(request: WSGIRequest, departure: str) -> HttpResponse:
    return render(request, 'departure.html')


def tour_view(request: WSGIRequest, id: int) -> HttpResponse:
    return render(request, 'tour.html')


def custom_handler404(request: WSGIRequest, exception) -> HttpResponse:
    return render(request, '404.html', status=400)


def custom_handler500(request: WSGIRequest) -> HttpResponse:
    return render(request, '500.html', status=500)
