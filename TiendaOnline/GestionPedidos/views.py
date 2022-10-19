from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormularioContacto
# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        producto = request.GET["prd"]
        if len(producto) > 20:
            mensaje = "Texto de busqueda excede limite establecido"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})
        # mensaje = "articulo buscado: %r" %request.GET["prd"]

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)
def contacto(request):
    if request.method=="POST":
        miForm =FormularioContacto(request.POST)
        if miForm.is_valid():
            infForm = miForm.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email',''),[infForm['email']],)
            return render(request, "gracias.html")
    else:
        miForm = FormularioContacto()

    return render(request, "Formulario_contacto.html", {'form':miForm})