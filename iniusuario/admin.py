from django.contrib import admin
from iniusuario import models

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("nombre","nombre_usu","cedula","tp_usu",)
    search_fields = ('TipoAdmin__nombre',)



admin.site.register(models.DatosUsuario,UsuarioAdmin)