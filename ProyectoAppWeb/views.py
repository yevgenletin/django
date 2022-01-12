from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from servicios.models import Servicios


# Create your views here.

def home(request):
    return render(request, "home.html")


def tienda(request):
    return render(request, "tienda.html")


def blog(request):
    return render(request, "blog.html")


def contacto(request):
    return render(request, "contacto.html")
