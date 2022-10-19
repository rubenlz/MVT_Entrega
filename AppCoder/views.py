from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar


def saludo(request): 
    return HttpResponse("hola mi primer app")
def otrosaludo(request):
    return HttpResponse("es otro saludo")
def saludara(request, nombre):
    return HttpResponse(f"hola como estas {nombre}")
def mostrarmitemplate(request):
    return render(request,"AppCoder/index.html")

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "AppCoder/familiares.html", {"lista_familiares": lista_familiares})