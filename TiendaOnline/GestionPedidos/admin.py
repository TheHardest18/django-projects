from django.contrib import admin
from GestionPedidos.models import Clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "email", "telefono")
    search_fields = ("nombre", "telefono")
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)
# Register your models here.
