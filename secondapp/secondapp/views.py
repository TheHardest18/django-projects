from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def Inicio(request):
    ctx = {}
    return render(request, "inicio.html", ctx)

def Home(request):
    obj = Persona("Isias", "Mateo")
    temas01 = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    ctx = {'nombre': obj.nombre, 'apdellido': obj.apellido, 'temas': temas01}
    return render(request,"miplantilla.html",ctx)
def iniciar(request):
    ctx = {}
    return render(request, "iniciar.html", ctx)
def edad(request):
    edad_actual = 18
    xpath = open("/home/thehardest18/Escritorio/Proyectos Django/secondapp/plantillas/hola.html")
    tmpl = Template(xpath.read())
    ctx = Context()
    documento = tmpl.render(ctx)
    xpath.close()
    return HttpResponse(documento)

def CalcularEdad(request, edad, anio ):
    # edad_actual = 18
    xpath = open("/home/thehardest18/Escritorio/Proyectos Django/secondapp/plantillas/edad.html")
    tmpl = Template(xpath.read())
    ctx = Context({'edad':edad, 'anio':anio})
    periodo = anio - 2022
    edad_futura = edad + periodo
    documento =tmpl.render(ctx)
    return  HttpResponse(documento)