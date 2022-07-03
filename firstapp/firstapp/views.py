import datetime
from django.template import Template, Context
from django.http import HttpResponse

def Home(request): #Denomina vista
    xpath = open("/home/thehardest18/Escritorio/Proyectos Django/firstapp/plantillas/hola.html")
    templ = Template(xpath.read())
    ctx = Context()
    documento = templ.render(ctx)
    xpath.close()
    return HttpResponse(documento)

def IniciarSesion(request):
    xpath = open("/home/thehardest18/Escritorio/Proyectos Django/firstapp/plantillas/iniciada.html")
    tmpl = Template(xpath.read())
    ctx = Context()
    documento = tmpl.render(ctx)
    return HttpResponse("Sesion Iniciada")

def Fecha(request):
    fecha_actual = datetime.datetime.now()
    doc_externo = open("/home/thehardest18/Escritorio/Proyectos Django/firstapp/plantillas/miplantilla.html")
    templ = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = templ.render(ctx)
    return HttpResponse(documento)

def CalcularEdad(request,edad, anio):

    # edad_actual = 18
    periodo = anio-2022
    edad_futura = edad + periodo
    documento = f"""<html>
        <body>
            <h2>En el anio: {anio} tendras {edad_futura} anios</h2>
        </body>
        </html>
        """
    return HttpResponse(documento)