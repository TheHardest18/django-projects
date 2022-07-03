from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def Home(request):
    obj = Persona("Isias", "Mateo")
    xpath = open("/home/thehardest18/Escritorio/Proyectos Django/secondapp/plantillas/miplantilla.html")
    tmpl = Template(xpath.read())
    ctx = Context({'nombre': obj.nombre, 'apellido': obj.apellido})
    documento = tmpl.render(ctx)
    return HttpResponse(documento)

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