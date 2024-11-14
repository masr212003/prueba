from django.contrib import admin
from Webprincipal import models

class VistaProducto(admin.ModelAdmin):
    list_display=("nombre","precio","id",)

class MarcaVista(admin.ModelAdmin):
    list_display=('nombreMar',)

class CategoriaVista(admin.ModelAdmin):
    list_display=('nombre',)


class OrdenVista(admin.ModelAdmin):
    list_display=('usuario','fecha','estado',)

admin.site.register(models.Categoria, CategoriaVista)
admin.site.register(models.Marca, MarcaVista)
admin.site.register(models.Productos,VistaProducto)
admin.site.register(models.CarritoProducto)
admin.site.register(models.Ordene, OrdenVista)
admin.site.register(models.OrdeneProducto)
