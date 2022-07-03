from django.http import HttpResponse
import datetime
from django.template import Template, Context

def Home(request):
    return HttpResponse("Hola mundo")

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