from django.shortcuts import render

# Create your views here.
from servicios.models import Servicios


def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, "servicios.html", {"servicios": servicios})

