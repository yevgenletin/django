from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request, "ProyectoAppWeb/template/home.html")


def servicios(request):
    return HttpResponse("Servicios")


def tienda(request):
    return HttpResponse("Tienda")


def blog(request):
    return HttpResponse("Blog")


def contacto(request):
    return HttpResponse("Contacto")

