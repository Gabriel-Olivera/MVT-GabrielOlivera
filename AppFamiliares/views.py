from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def familiares(request):
    familiar1=Familiares (nombre="Martin",tipo="Padre",edad=50,fecha_nacimiento="1972-01-01")
    familiar1.save()
    texto1=f"{familiar1.nombre} - {familiar1.tipo} - {familiar1.edad} - {familiar1.fecha_nacimiento}"

    familiar2=Familiares (nombre="Laura",tipo="Madre",edad=47,fecha_nacimiento="1975-12-12")
    familiar2.save()
    texto2=f"{familiar2.nombre} - {familiar2.tipo} - {familiar2.edad} - {familiar2.fecha_nacimiento}"
    
    familiar3=Familiares (nombre="Jose",tipo="Hijo",edad=12,fecha_nacimiento="2010-07-03")
    familiar3.save()
    texto3=f"{familiar3.nombre} - {familiar3.tipo} - {familiar3.edad} - {familiar3.fecha_nacimiento}"

    texto=texto1+", "+texto2+", "+texto3

    return HttpResponse(texto)
