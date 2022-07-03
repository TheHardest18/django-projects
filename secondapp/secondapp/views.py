from django.http import HttpResponse
import datetime
from django.template import Template, Context

def Home(request):
    return HttpResponse("Hola mundo")

def edad(request):
    edad_actual = 18
    documento = f"""<html>
        <body>
            <h1>tu edad es de {edad_actual}</h1>
        </body>
    </html>"""
    return HttpResponse(documento)

def CalcularEdad(request, anio, edad_actual):
    # edad_actual = 18
    pass
